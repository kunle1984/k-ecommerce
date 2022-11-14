
let wishlistCount=document.getElementById("wishlistcount")
let wishlist={}
if(localStorage.getItem('wishlist')==null){
    localStorage.setItem('wishlist', JSON.stringify(wishlist))

}else{
    wishlist=JSON.parse(localStorage.getItem('wishlist'))
    wishlistCount.innerHTML=Object.keys(wishlist).length
  
   
}


 $(document).on('click', '.btn-wishlist', function(){
    let item_id=this.id.toString();
    if(wishlist[item_id]!=undefined){
    let   quantity=wishlist[item_id][0]+1
    wishlist[item_id][0]=quantity
      
    }else{
        quantity=1
        
        pname=document.getElementById("n"+item_id).innerHTML
        pprice=document.getElementById("p"+item_id).innerHTML
        imageUrl=document.getElementById("image"+item_id).innerHTML

        wishlist[item_id]=[quantity,pname,pprice,imageUrl]
      
    }
    localStorage.setItem('wishlist', JSON.stringify(wishlist))

    wishlistCount.innerHTML=Object.keys(wishlist).length
   

console.log(wishlist);

console.log(Object.keys(wishlist).length)
})
DisplayWishlist(wishlist)
function DisplayWishlist(wishlist){
    let showWishList=''
   
    n=0
    for(let x in wishlist){
       
        showWishList+=` <tr>
        <td class="product-col">
            <div class="product">
                <figure class="product-media">
                    <a href="#">
                        <img src=${wishlist[x][3]}/>
                    </a>
                    <div id="image${x}" class="d-none">${wishlist[x][3]}</div>
                </figure>

                <h3 class="product-title">
                    <a id="n${x}" href="#">${wishlist[x][1]}</a>
                </h3><!-- End .product-title -->
            </div><!-- End .product -->
        </td>
        <td id="p${x}"   class="price-col">${wishlist[x][2]}</td>
        
        <td ><button  id="${x}" class="btn-product btn-cart">Add to cart</button></td>
    </tr>`
  n++
    }
    
    document.getElementById("wishView").innerHTML=showWishList
  
 }


 $(document).on('click', '#clearWish', function(){
    console.log('clicked')
    localStorage.removeItem('wishlist');
  })
  

 


  