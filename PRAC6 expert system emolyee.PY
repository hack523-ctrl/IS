# Expert system on Employee performance evaluation using python

class Employee:
    def __init__(self, name, punctuality, task_completion, teamwork, innovation):
        self.name = name
        self.punctuality = punctuality        
        self.task_completion = task_completion  
        self.teamwork = teamwork              
        self.innovation = innovation          
def evaluate_performance(employee):
    avg_score = (employee.punctuality + employee.task_completion +
                 employee.teamwork + employee.innovation) / 4
    if avg_score >= 9:
        level = "Outstanding"
        advice = "Recommend promotion and bonus."
    elif avg_score >= 7:
        level = "Excellent"
        advice = "Maintain performance and consider for future leadership roles."
    elif avg_score >= 5:
        level = "Satisfactory"
        advice = "Encourage improvement in weaker areas."
    else:
        level = "Needs Improvement"
        advice = "Recommend training and closer supervision."
    return level, advice
def get_employee_input():
    name = input("Enter employee name: ")
    punctuality = int(input("Rate punctuality (1-10): "))
    task_completion = int(input("Rate task completion (1-10): "))
    teamwork = int(input("Rate teamwork (1-10): "))
    innovation = int(input("Rate innovation (1-10): "))
    return Employee(name, punctuality, task_completion, teamwork, innovation)
def main():
    print("Employee Performance Evaluation Expert System")
    emp = get_employee_input()
    level, advice = evaluate_performance(emp)
    print("\n--- Evaluation Result ---")
    print(f"Employee Name: {emp.name}")
    print(f"Performance Level: {level}")
    print(f"System Advice: {advice}")
if __name__ == "__main__":
    main()