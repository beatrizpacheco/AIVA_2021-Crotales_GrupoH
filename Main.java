package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.awt.Image;
import javax.swing.ImageIcon;

public class Main {
    public static void main(String[] args) throws IOException {
        //Introducir la ruta global de la imagen del crotal en el archivo main.sh
        ProcessBuilder builder = new ProcessBuilder("bash", "main.sh");
        Process process = builder.start();

        InputStream stdout = process.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(stdout));
        String crotal;// = reader.readLine();
        while ((crotal = reader.readLine()) != null){
            System.out.println(crotal);
        }
    }
}