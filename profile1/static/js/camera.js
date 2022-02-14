/*const constraints = window.constraints = {
    audio: true,
    video: true
   };

async function openCamera(e) {
    
    
    const stream = await 
    navigator.mediaDevices.getUserMedia(constraints);
    
    gotStream(stream);
    e.target.disabled = true;
    }  
    function gotStream(stream) {
        const videoEle = document.querySelector('video');
        const videoTracks = stream.getVideoTracks();
        showMsg(`Device in use: ${videoTracks[0].label}`);
        window.stream = stream;
        videoEle.srcObject = stream;
       }*/



function startCall(){
    document.getElementById("video-call-div").style.display = "inline"

    navigator.getUserMedia({
        
        video: {
            frameRate: 24,
            width: {
                min: 480, ideal: 720, max:1280
            },
            aspectRatio: 1.33333
        },
        audio: true
    }, (stream) => {
            localStream = stream
            document.getElementById("local-video").srcObject = localStream
    }, (error) => {
        console.log(error);
    })
}