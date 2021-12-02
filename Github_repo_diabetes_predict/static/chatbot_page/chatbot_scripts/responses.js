function getBotResponse(input) {
    //rock paper scissors
    input=input.toLowerCase();
    if (input == "doctor") {
        return "visit our contact page";
    }
    else if (input == "exercise") {
        return "visit this blog https://www.niddk.nih.gov/health-information/diabetes/overview/diet-eating-physical-activity";
    } 
    else if (input == "diet") {
        return "visit this blog https://www.niddk.nih.gov/health-information/diabetes/overview/diet-eating-physical-activity";
    } 
    else if (input == "stats") {
        return "visit this blog https://www.livemint.com/science/health/government-survey-found-11-8-prevalence-of-diabetes-in-india-11570702665713.html";
    }
    else if (input == "symptoms") {
        return "visit this blog https://www.mayoclinic.org/diseases-conditions/diabetes/symptoms-causes/syc-20371444";
    } 
    else if (input == "prevention and treatment") {
        return "visit this blog https://www.healthline.com/health/diabetes#prevention";
    } 
    else if (input == "prediction parameters") {
        return "Which parameter information you want: Glucose Level / Insulin / BMI / Diabetes Pedigree Function ?";
    } 
    else if (input == "insulin") {
        return "visit this blog https://www.healthline.com/health/type-2-diabetes/insulin";
    } 
    else if (input == "bmi") {
        return "visit this blog https://en.wikipedia.org/wiki/Body_mass_index";
    } 
    else if (input == "glucose level") {
        return "visit this blog https://medlineplus.gov/bloodsugar.html";
    } 
    else if (input == "blood pressure") {
        return "visit our FAQ section in predict page";
    } 
    else if (input == "general info") {
        return "visit this blog https://www.niddk.nih.gov/health-information/diabetes/overview/what-is-diabetes";
    } 

    // Simple responses
    else if (input == "hello" || "hi" || "hola" || "hey"||"fine"||"nice"||"good"||"great") {
        return "Hello there! what you want to ask about regarding diabetes: general info / symptoms / prevention and treatment / Doctor / Exercise / Diet / stats /prediction parameters?";
    } 
    else if (input == "goodbye"||"bye"||"thanks") {
        return " Thanks for using our services, Talk to you later!";
    } 
    else {
        return "Try asking something else!";
    }
}