
const mycaller_button  = document.querySelector("#myvidcaller-button")
mycaller_button.addEventListener("click",(event)=>{
    $("#message-box1").hide(1500)
    $(".video-container").show(2500)
    let constraintsObj = {
        audio:true,
        video:{
            facingMode:'user',
            width:{min:640,ideal:1280,max:1920},
            height:{min:480,ideal:720,max:1080}
        }
    }
    
    navigator.mediaDevices.getUserMedia(constraintsObj).then(function(mediaStreamObj){
        let video = document.querySelector('video')
        if("srcObject" in video){
            video.srcObject = mediaStreamObj
        }
        else{
            video.src = window.URL.createObjectURL(mediaStreamObj)
        }
        video.onloadedmetadata = function(ev){
            video.play()
        }
        let dcb = document.querySelector('#endcall_butt')
        dcb.addEventListener("click",function(){
            mediaStreamObj.getTracks().forEach((track) => {
                track.stop();
                $("#message-box1").show(1500)
                $(".video-container").hide(2500)
                });
        })
    }).catch(function(err){
        console.log(err.name,err.message)
    })

})