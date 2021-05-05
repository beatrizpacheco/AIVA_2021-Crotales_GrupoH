package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        ProcessBuilder builder = new ProcessBuilder("C:\\EjemploAI\\main.bat");
        Process process = builder.start();

        InputStream stdout = process.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(stdout));
        String crotal;// = reader.readLine();
        while ((crotal = reader.readLine()) != null){
            System.out.println(crotal);
        }
    }
}