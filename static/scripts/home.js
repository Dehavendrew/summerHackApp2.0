function test(){
  var face = document.getElementById("face")

  if(face.style.visibility == 'visible'){
    face.style.visibility = 'hidden'
    return
  }
  if(face.style.visibility == 'hidden'){
    face.style.visibility = 'visible'
    return
  }
}
