import java.io.FileNotFoundException; 
import java.io.FileReader; 
import java.io.IOException; 
import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Arrays;


public class Housing_parser{

    ArrayList<Group> housing = new ArrayList<Group>();

	public  void load_doc(){
		FileReader fileName;
        
        try {
            fileName = new FileReader("../housing 2020.csv"); //csv filename goes here
            Scanner scnr = new Scanner(fileName);
            scnr.useDelimiter(",");
            while(scnr.hasNextLine()) {
                String[] line = scnr.nextLine().split(",");
                if(line.length != 5)
                    continue;

                double pointVal = Double.parseDouble(line[1]);
                int groupSize = Integer.parseInt(line[2]);
                String selTime = line[3];
                int lotNum = Integer.parseInt(line[4]);
                Group group = new Group(pointVal, groupSize, lotNum, selTime);
                
                housing.add(group);
                

                // System.out.println(group.ptVal);
            }
            scnr.close();
        }
        catch(IOException e){
            e.printStackTrace();
        }
    }
    
    public int getHousingIdx(int housingNumber){  // gets index of your housing number
        for(int i = 0; i < housing.size(); i++){
            if (housing.get(i).lottoNum == housingNumber)
                return i;
        }
        return -1;
    }
    public void getHousStats(int hIdx){
        getHousStats(hIdx, new Integer[]{8}, 0);
    }

    public void getHousStats(int hIdx, Integer[] groupSize, double points){
        //  usage: getHousStats(housing #) will return groups of 8 members before you 
        //         getHousStats((8,9), 20) returns groups of 9 or 10 members
        //         getHousStats((9), 20) groups with only 9 members and so on
        //         points variable shows only groups >= to that value
        HashSet<Integer> gSize = new HashSet<>(Arrays.asList(groupSize));
        int tally = 0;
        for(int i = 0 ; i  < hIdx; i++){ // index through groups
            if( housing.get(i).ptVal >= points  && gSize.contains(housing.get(i).size) ){
                System.out.println(housing.get(i));
                tally += 1;
            }

        }  
        System.out.println("\n" + tally + "  groups before you \n");
    }

    public static void main(String[] args){
        
        Housing_parser hp = new Housing_parser();
        hp.load_doc();
        int housingNumber = 2266; // input your housing number
        int hIdx = hp.getHousingIdx(housingNumber); // our housing number index
        Integer[] gSize = {8,9,10};

        System.out.println("Groups of 8,9:");
        hp.getHousStats(hIdx, new Integer[]{8,9}, 20); // same as getHousStats(hIdx)

        hp.getHousStats(hIdx);

    }

}