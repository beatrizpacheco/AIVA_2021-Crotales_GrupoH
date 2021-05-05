package com.company;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.awt.Image;
import javax.swing.ImageIcon;

public class Main {
    public static void main(String[] args) throws IOException {
        //Introducir la ruta global de la imagen del crotal
        String image_crotal = new String("C:\\EjemploAI\\AIVA_2021-Crotales_GrupoH\\TestSamples/0001.TIF");
        ProcessBuilder builder = new ProcessBuilder("C:\\EjemploAI\\main.bat",image_crotal);
        Process process = builder.start();

        InputStream stdout = process.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(stdout));
        String crotal;// = reader.readLine();
        while ((crotal = reader.readLine()) != null){
            System.out.println(crotal);
        }
    }
}