package thisex;

class Birthday{
    int day, month, year;

    public void setYear(int year){
        this.year=year;

    }
    public void printThis(){
        System.out.println(this);
    }
}

public class thisex{
    public static void main(String[]args){
        Birthday bDay=new Birthday();
        bDay.setYear(2000);
        System.out.println(bDay);
        bDay.printThis();
    }
}