
//let r=document.getElementById("r")

 
  $(document).on('click', '.btn-block', function(){
    console.log('clicked')
    console.log(document.getElementById("r").value)
    if(document.getElementById("r").value=="r"){

        localStorage.removeItem('cart');
    }else{

    }
   
  })
  

  
 