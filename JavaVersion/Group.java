

public class Group{

    public double ptVal;
    public int size;
    public String time;
    public int lottoNum;

    public Group(double ptVal, int size, int lottoNum, String time){
        this.ptVal = ptVal;
        this.size = size;
        this.lottoNum = lottoNum;
        this.time = time;
    }

    public String toString(){
        return String.format("%f  %d  %d  %s", ptVal, size, lottoNum, time);
    }

}