/*
 * Copyright 2005-2015 WSO2, Inc. (http://wso2.com)
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *     http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.wso2.ppaas.configurator.tests;

import org.apache.commons.exec.*;
import org.apache.commons.io.FileUtils;
import org.apache.commons.lang.StringUtils;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.w3c.dom.Document;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.*;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

/**
 * Test Manager Class for Configurator integration testing
 */
public class ConfiguratorTestManager {
    public static final String PATH_SEP = File.separator;
    private static final Log log = LogFactory.getLog(ConfiguratorTestManager.class);
    public static final String DISTRIBUTION_PATH = "distribution.path";
    public static final String DISTRIBUTION_NAME = "distribution.name";
    public static final String TEMPLATE_MODULES = "template-modules";
    protected String distributionPath;
    protected String distributionName;
    protected final UUID CONFIGURATOR_DIR_NAME = UUID.randomUUID();
    public final long TIMEOUT = 180000;

    public ConfiguratorTestManager() {
        distributionPath = System.getProperty(DISTRIBUTION_PATH);
        distributionName = System.getProperty(DISTRIBUTION_NAME);
        log.info("Configurator distribution name: " + distributionPath);
    }

    protected static String getResourcesPath() {
        return ConfiguratorTestManager.class.getResource(PATH_SEP).getPath() + PATH_SEP + ".." + PATH_SEP + ".."
                + PATH_SEP + "src" + PATH_SEP + "test" + PATH_SEP + "resources";
    }

    protected static String getResourcesPath(String resourcesPath) {
        return ConfiguratorTestManager.class.getResource(PATH_SEP).getPath() + ".." + PATH_SEP + ".." + PATH_SEP + "src"
                + PATH_SEP + "test" + PATH_SEP + "resources" +
                PATH_SEP + resourcesPath;
    }

    /**
     * Copy Configurator distribution to a new folder, extract it and copy sample
     * configuration files
     *
     * @return Configurator destination Path
     */
    protected String setupConfigurator(String resourcesPath) {
        try {
            log.info("Setting up Configurator...");
            String unzipDestPath = ConfiguratorTestManager.class.getResource(PATH_SEP).getPath() + PATH_SEP +
                    ".." + PATH_SEP + CONFIGURATOR_DIR_NAME + PATH_SEP;
            unzip(distributionPath, unzipDestPath);
            String destConfiguratorPath = ConfiguratorTestManager.class.getResource(PATH_SEP).
                    getPath() + PATH_SEP + ".." + PATH_SEP + CONFIGURATOR_DIR_NAME + PATH_SEP + distributionName;

            String srcConfiguratorConfPath = getResourcesPath(resourcesPath) + PATH_SEP +
                    TEMPLATE_MODULES;
            String destConfiguratorConfPath = destConfiguratorPath + PATH_SEP + TEMPLATE_MODULES;
            FileUtils.copyDirectory(new File(srcConfiguratorConfPath), new File(destConfiguratorConfPath));

            log.info("Configurator setup completed");

            return destConfiguratorPath;
        } catch (Exception e) {
            String message = "Could not setup configurator distribution";
            log.error(message, e);
            throw new RuntimeException(message, e);
        }
    }

    private void unzip(String zipFilePath, String destDirectory) throws IOException {
        File destDir = new File(destDirectory);
        if (!destDir.exists()) {
            destDir.mkdir();
        }
        ZipInputStream zipIn = new ZipInputStream(new FileInputStream(zipFilePath));
        ZipEntry entry = zipIn.getNextEntry();
        // iterates over entries in the zip file
        while (entry != null) {
            String filePath = destDirectory + File.separator + entry.getName();
            if (!entry.isDirectory()) {
                // if the entry is a file, extracts it
                extractFile(zipIn, filePath);
            } else {
                // if the entry is a directory, make the directory
                File dir = new File(filePath);
                dir.mkdir();
            }
            zipIn.closeEntry();
            entry = zipIn.getNextEntry();
        }
        zipIn.close();
    }

    private void extractFile(ZipInputStream zipIn, String filePath) throws IOException {
        BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(filePath));
        byte[] bytesIn = new byte[4096];
        int read;
        while ((read = zipIn.read(bytesIn)) != -1) {
            bos.write(bytesIn, 0, read);
        }
        bos.close();
    }

    public void setup(String resourcePath, Map<String, String> environment) {
        String configuratorPath = setupConfigurator(resourcePath);
        log.info("Configurator working directory name: " + CONFIGURATOR_DIR_NAME);
        log.info("Starting configurator ...");
        int result = executeCommand("python " + configuratorPath + PATH_SEP + "configurator.py", environment);
        if (result != 0) {
            throw new RuntimeException("Configurator returned with non-zero exit code");
        }
    }

    /**
     * Sleep current thread
     *
     * @param time Time to sleep in milli-seconds
     */
    protected void sleep(long time) {
        try {
            Thread.sleep(time);
        } catch (InterruptedException ignore) {
        }
    }

    /**
     * Return new lines found in the output
     *
     * @param currentOutputLines current output lines
     * @param output             output
     * @return new lines printed by Python agent process
     */
    protected List<String> getNewLines(List<String> currentOutputLines, String output) {
        List<String> newLines = new ArrayList<String>();

        if (StringUtils.isNotBlank(output)) {
            String[] lines = output.split(System.lineSeparator());
            for (String line : lines) {
                if (!currentOutputLines.contains(line)) {
                    currentOutputLines.add(line);
                    newLines.add(line);
                }
            }
        }
        return newLines;
    }

    protected void tearDown() {

    }

    public String readXML(String resourcePath, String xpathExpression) {

        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = null;
        try {
            String targetFile = ConfiguratorTestManager.class.getResource(PATH_SEP).getPath() + ".." + PATH_SEP
                    + CONFIGURATOR_DIR_NAME + PATH_SEP + resourcePath;
            builder = factory.newDocumentBuilder();
            Document doc = builder.parse(targetFile);
            XPathFactory xPathfactory = XPathFactory.newInstance();
            XPath xpath = xPathfactory.newXPath();
            XPathExpression expr = xpath.compile(xpathExpression);
            String value = expr.evaluate(doc, XPathConstants.STRING).toString();
            log.info("Parsed value" + value);
            return value;

        } catch (ParserConfigurationException | SAXException | IOException |
                XPathExpressionException e) {
            log.error("Error in parsing xml " + e.getMessage());
        }
        return null;
    }

    /**
     * Execute shell command
     *
     * @param commandText command to be executed
     * @param environment map of environmental variables to be passed to the process
     */
    protected int executeCommand(final String commandText, Map<String, String> environment) {
        final ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        final int[] result = new int[1];
        final boolean[] hasProcessEnded = { false };
        try {
            CommandLine commandline = CommandLine.parse(commandText);
            DefaultExecutor exec = new DefaultExecutor();
            PumpStreamHandler streamHandler = new PumpStreamHandler(outputStream);
            exec.setWorkingDirectory(new File(ConfiguratorTestManager.class.getResource(PATH_SEP).getPath() +
                    ".." + PATH_SEP + CONFIGURATOR_DIR_NAME));
            exec.setStreamHandler(streamHandler);
            ExecuteWatchdog watchdog = new ExecuteWatchdog(TIMEOUT);
            exec.setWatchdog(watchdog);
            exec.execute(commandline, environment, new ExecuteResultHandler() {
                @Override
                public void onProcessComplete(int i) {
                    log.info(commandText + " process completed with return code: " + i);
                    result[0] = i;
                    hasProcessEnded[0] = true;
                }

                @Override
                public void onProcessFailed(ExecuteException e) {
                    log.error(commandText + " process failed", e);
                    hasProcessEnded[0] = true;
                }
            });

            List<String> outputLines = new ArrayList<>();
            List<String> newLines;
            while (!hasProcessEnded[0] | ((newLines = getNewLines(outputLines, outputStream.toString())).size() > 0)) {
                for (String line : newLines) {
                    if (line.contains("Exception in thread") || line.contains("ERROR")) {
                        try {
                            throw new RuntimeException(line);
                        } catch (Exception e) {
                            log.error("Error found in configurator log", e);
                        }
                    }
                    log.info("[CONFIGURATOR] " + line);
                }

                sleep(1000);
            }
            return result[0];
        } catch (Exception e) {
            log.error(outputStream.toString(), e);
            throw new RuntimeException(e);
        }
    }
}
