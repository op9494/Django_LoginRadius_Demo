const url = window.location.href;
const action=window.location.href.split("/")[3];
console.log("url split",action)
maindomine="http://127.0.0.1:8000/"
if(action=="login"){
    const tokenwt = url.split("?")[1];
    const access_token=tokenwt.split("=")[1];
    const domainName = url.substring(0, url.lastIndexOf("/"));
    console.log(access_token,domainName)
    localStorage.setItem("lr-session-token", access_token);
    setCookie("lr-session-token",access_token, "No days")
    
    if(localStorage.getItem("lr-session-token") !=null && access_token!=""){
        window.location.href = maindomine + "dashboard";
    }
    else{
        window.location.href = maindomine ; 
    }
}

if(action=="logout"){
    window.localStorage.clear();
    console.log("storage cleared")
    window.location.href = maindomine;
}
if(action=="fp"){
    actionmsg=url.split("?")[1]
    console.log("splitacto",url)
    if (actionmsg=="action_completed=forgotpassword"){
        alert("For resetting password mail has been sent to Your mail id")
        window.location.href = maindomine;
    }
    else{
        alert("Sorry!! please try again")
        window.location.href = maindomine;
    }
   
}
if(action=="register"){
        window.location.href = maindomine ;
}


function setCookie(cname, cvalue, exdays) {
    var d = new Date(); 
    d.setTime(d.getTime() + (exdays* 24 * 60 * 60 * 1000)); 
    var expires = "expires="+d.toUTCString(); 
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/"; 
    }