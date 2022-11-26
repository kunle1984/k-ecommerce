cart=JSON.parse(localStorage.getItem('cart'))
document.getElementById("order").value=JSON.stringify(cart)
orderCart()

function orderCart(){
    totalCost=0
    let showOrderCart=''
    let cartProduct=''
for(let x in cart){
    cartProduct+=' '+`${cart[x][1]}: $ ${cart[x][2]}`
    totalCost+=parseFloat(cart[x][2])*parseInt(cart[x][0])
    showOrderCart+=`<tr>
    <td><a href="#">${cart[x][1]}</a></td>
    <td>${parseFloat(cart[x][2])*parseInt(cart[x][0])}</td>
</tr>`

}

document.getElementById("product_bought").value=cartProduct
document.getElementById("pro_summary").innerHTML=showOrderCart
document.getElementById("subTotal").textContent='$ '+totalCost
document.getElementById("TotalOrder").textContent='$ '+totalCost
document.getElementById("orderAmount").value=totalCost

  }
