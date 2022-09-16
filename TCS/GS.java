
public class GS {
    private String name="Vinod";
    private int EmpID=213020; 

    

    public GS(String name,int EmpID){
        this.name=name;
        this.EmpID=EmpID;
        
    }

    public String getName(){
        return name;
    }
    public String setName(String name){
       return this.name=name;
    }

    public int getEmpID() {
        return EmpID;
    }

    public void setEmpID(int empID) {
        EmpID = empID;
    }
    
}
