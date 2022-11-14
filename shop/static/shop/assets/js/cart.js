const cartBtn=document.getElementsByClassName(".carts-btn")
let cartCount=document.getElementById("countCart")
let cart={}
if(localStorage.getItem('cart')==null){
    localStorage.setItem('cart', JSON.stringify(cart))
    

}else{
   

    cart=JSON.parse(localStorage.getItem('cart'))
    cartCount.innerHTML=Object.keys(cart).length
}


 $(document).on('click', '.btn-product', function(){
    //DisplayCart(cart)
    let item_id=this.id.toString();
    if(cart[item_id]!=undefined){
    let   quantity=cart[item_id][0]+1
       cart[item_id][0]=quantity
     
       DisplayCart(cart)
      
    }else{
        quantity=1
        
        pname=document.getElementById("n"+item_id).innerHTML
        pprice=document.getElementById("p"+item_id).innerHTML
        imageUrl=document.getElementById("image"+item_id).innerHTML

        cart[item_id]=[quantity,pname,pprice,imageUrl]
       
    }
    localStorage.setItem('cart', JSON.stringify(cart))

    cartCount.innerHTML=Object.keys(cart).length
   
   
console.log(cart);

console.log(Object.keys(cart).length)
})

cartCount.innerHTML=Object.keys(cart).length 
DisplayCart(cart)
function DisplayCart(cart){
   let cartString=''
   let totalCost=0
   for(let x in cart){

    totalCost+=parseFloat(cart[x][2])*parseInt(cart[x][0])
    cartString+=` <div class="product">
    <div class="product-cart-details">
        <h4 class="product-title">
            <a href="product.html">${cart[x][1]}</a>
        </h4>

        <div class="cart-product-info">
            <span class="cart-product-qty">${cart[x][0]}</span>
            x ${cart[x][2]}
        </div>
    </div>

    <figure class="product-image-container">
        <a href="product.html" class="product-image">
            <img src=${cart[x][3]} alt="product">
        </a>
    </figure>
    <a href="#" class="btn-remove" title="Remove Product"><i class="icon-close"></i></a>
</div>`

   }
cartCount.innerHTML=Object.keys(cart).length 
document.getElementById("cartDropDown").innerHTML=cartString
document.getElementById("totalCost").textContent='$ '+totalCost

}


 function DisplayViewCart(cart){
    let showCart=''
    totalCost=0
    n=0
    for(let x in cart){
        totalCost+=parseFloat(cart[x][2])*parseInt(cart[x][0])
        showCart+=` <tr>
        <td class="product-col">
            <div class="product">
                <figure class="product-media">
                    <a href="#">
                        <img src=${cart[x][3]}>
                    </a>
                </figure>

                <h3 class="product-title">
                    <a id="pro${n}" href="#">${cart[x][1]}</a>
                </h3><!-- End .product-title -->
            </div><!-- End .product -->
        </td>
        <td  class="price-col">${cart[x][2]}</td>
        <td class="quantity-col">
            <div class="cart-product-quantity">
                <input id="productNum${x}" type="number" class="form-control" value="${cart[x][0]}"min="1"  step="1" data-decimals="0" required>
            </div><!-- End .cart-product-quantity -->
        </td>
        <td class="total-col">${parseFloat(cart[x][2])*parseInt(cart[x][0])}</td>
        <td class="remove-col"><button  id="${x}" class="btn-remove"><!--<i class="icon-close"></i>--></button></td>
    </tr>`
  n++
    }
    document.getElementById("subTotal").textContent='$ '+totalCost
    document.getElementById("finalTotal").textContent='$ '+totalCost
    document.getElementById("cartView").innerHTML=showCart
  
 }

 function updateCart(cart){
    let showCart=''
    totalCost=0
    n=0
    for(let x in cart){
        totalCost+=parseFloat(cart[x][2])*parseInt(cart[x][0])
        showCart+=` <tr>
        <td class="product-col">
            <div class="product">
                <figure class="product-media">
                    <a href="#">
                        <img src=${cart[x][3]}>
                    </a>
                </figure>

                <h3 class="product-title">
                    <a id="pro${n}" href="#">${cart[x][1]}</a>
                </h3><!-- End .product-title -->
            </div><!-- End .product -->
        </td>
        <td  class="price-col">${cart[x][2]}</td>
        <td class="quantity-col">
            <div class="cart-product-quantity">
                <input id="productNum${x}" type="number" class="form-control" value="${cart[x][0]}"min="1"  step="1" data-decimals="0" required>
            </div><!-- End .cart-product-quantity -->
        </td>
        <td class="total-col">${parseFloat(cart[x][2])*parseInt(cart[x][0])}</td>
        <td class="remove-col"><button  id="${x}" class="btn-remove"><i class="icon-close"></i></button></td>
    </tr>`
  n++
  return showCart
    }
   

 }


 $(document).on("click", "#refreshCart", function(){
    newTotalCost=0
    console.log('hello you press me')
    for(let x in cart){
      
        prodNum=parseInt(document.getElementById(`productNum${x}`).value)
        newCost=prodNum*parseFloat(cart[x][2])
        cart[x][0]=prodNum
        updateCart(cart)
      
   
    }
    localStorage.setItem('cart', JSON.stringify(cart))
    cartCount.innerHTML=Object.keys(cart).length
    document.getElementById("cartView").innerHTML=showCart
    
 })

 
 /**($(document).on('click', '.btn-remove', function(){
    console.log('remove item clicked')
 
    let new_id=this.id.toString()
    console.log('the id is ', new_id)
 dataItems={}
newArray=Object.assign([],  cart)
 //array2=['a', 'b', 'c'].reduce((a, v) => ({ ...a, [v]: v}), {}) 
    for(let  x in cart ){
        dataItems[x]=cart[x]
        if(x===new_id){
           delete cart.new_id
        
          }
          
          
     // console.log('real id',x)
     // console.log('picked id',new_id)
    }

    console.log(newArray)


   
  //localStorage.setItem('cart', JSON.stringify(cart))


 
   
  })
**/
 
  $(document).on('click', '#clearCart', function(){
    console.log('clicked')
    localStorage.removeItem('cart');
  })
  

