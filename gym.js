function home(){
    document.getElementById("Home").style.color="green";
    document.getElementById("Plan").style.color="white";
    document.getElementById("Contact").style.color="white";
    document.getElementById("Blog").style.color="white";
    document.getElementById("Program").style.color="white";

}

function program(){
    document.getElementById("Home").style.color="white";
    document.getElementById("Plan").style.color="white";
    document.getElementById("Contact").style.color="white";
    document.getElementById("Blog").style.color="white";
    document.getElementById("Program").style.color="green";

}
function plan(){
    document.getElementById("Home").style.color="white";
    document.getElementById("Plan").style.color="green";
    document.getElementById("Contact").style.color="white";
    document.getElementById("Blog").style.color="white";
    document.getElementById("Program").style.color="white";

}
function blog(){
    document.getElementById("Home").style.color="white";
    document.getElementById("Plan").style.color="white";
    document.getElementById("Contact").style.color="white";
    document.getElementById("Blog").style.color="green";
    document.getElementById("Program").style.color="white";

}
function contact(){
    document.getElementById("Home").style.color="white";
    document.getElementById("Plan").style.color="white";
    document.getElementById("Contact").style.color="green";
    document.getElementById("Blog").style.color="white";
    document.getElementById("Program").style.color="white";

}

// submit

function submit(){
    let name = document.getElementById("Name");
    let number = document.getElementById("Number");

    if(name.value == ""){
        alert("Please Enter Name")
    }else if(number.value == ""){
        alert("Please Enter Number")
    }else{
        alert("Thanks For Join : " + name.value)
    }
}