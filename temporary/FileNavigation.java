/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Arthur
 * Date:08/03/2016
 */


import java.awt.Dimension;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.FileReader;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

/**
* Opens A File by the Adress (String ende) and what to write in it (StringtoWrite)
* If archive doesnt exist it creats and writes in it
*/
public class FileNavigation {
    private File arqv;
    FileNavigation(String ende){
        arqv = new File(ende);
        try{
            if (!arqv.exists()){// if it doesnt exist IT CREATES
                arqv.getParentFile().mkdirs();//.createNewFile();
            }
        } catch (Exception e){
            e.printStackTrace();
        }
         
    }
    public void fileWrite(String toWrite){        
        try{
            if(!(checkExistence(toWrite))){
                FileWriter fw = new FileWriter(arqv,true);
                BufferedWriter bw = new BufferedWriter(fw);
                bw.write(toWrite); //escrevo o que quero
                bw.newLine(); // adiciona mais uma linha no final (um enter)

                bw.close();
                fw.close();// "Flush" do python
            }
            else{ //TO DO
                //popUp Louco
                System.out.println("Deu ruim, arquivo já existe");
            }
            
        } catch (Exception e){
            e.printStackTrace();
        }
    }
   
    public String fileRead(){
        String saver = "";
        try{
            FileReader fr = new FileReader(arqv);
            BufferedReader buffRead = new BufferedReader(fr);
            String linha = "";
            //String saver = "";
            
            while(linha != null){
                linha = buffRead.readLine();// passa para a proxima linha
                if(linha != null){
                    saver += linha;
                    saver += '\n';
                }
                
            }
            //return saver;
            
        } catch (Exception e){
            e.printStackTrace();
        }
        return saver;
    }
    
    public void fileShow(String message){
        //String message = fileRead();
        final JTextArea textArea = new JTextArea();
        JScrollPane scrollPane = new JScrollPane(textArea);
        textArea.setEditable(false);
        
        textArea.setText(message);
        scrollPane.setPreferredSize(new Dimension(350, 550));
        JOptionPane.showMessageDialog(null,scrollPane,"Culture Reader",JOptionPane.PLAIN_MESSAGE);
    }
    
    
    
    
    private boolean checkExistence(String toCheck){ //checka se a string passado, ja foi salva antes
        try{
            FileReader fr = new FileReader(arqv);
            BufferedReader buffRead = new BufferedReader(fr);
            String linha = "";
            String comp1,comp2;
            comp2 = toCheck.toLowerCase();
            while (linha!=null){ // se a linha tiver vazia é pq acabou 
                linha = buffRead.readLine();// passa para a proxima linha
                comp1 = linha.toLowerCase();
                
                if(comp1.equals(comp2)){
                    return true;
                }
            }
            buffRead.close();
            fr.close();// "Flush" do python
            return false;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
    public File getArqv(){
        return arqv;
}
    
}
