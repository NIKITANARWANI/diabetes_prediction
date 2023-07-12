#Usage of Model
import pickle
import warnings
warnings.filterwarnings("ignore")

f=open("de.model","rb")
model=pickle.load(f)

pr=float(input("Enter Pregnancies: "))
gl=float(input("Enter Glucose: "))
bp=float(input("Enter BloodPressure: "))
st=float(input("Enter SkinThickness: "))
ins=float(input("Enter Insulin: "))
bmi=float(input("Enter BMI: "))
dp=float(input("Enter DiabetesPedigreeFunction: "))
age=float(input("Enter Age: "))
data=[[pr,gl,bp,st,ins,bmi,dp,age]]
yn=model.predict(data)
print("Diabetes",yn)