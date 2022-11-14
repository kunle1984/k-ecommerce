cart=JSON.parse(localStorage.getItem('cart'))
document.getElementById("order").value=JSON.stringify(cart)
orderCart()

function orderCart(){
    totalCost=0
    let showOrderCart=''
for(let x in cart){
    totalCost+=parseFloat(cart[x][2])*parseInt(cart[x][0])
    showOrderCart+=`<tr>
    <td><a href="#">${cart[x][1]}</a></td>
    <td>${parseFloat(cart[x][2])*parseInt(cart[x][0])}</td>
</tr>`

}
document.getElementById("pro_summary").innerHTML=showOrderCart
document.getElementById("subTotal").textContent='$ '+totalCost
document.getElementById("TotalOrder").textContent='$ '+totalCost
document.getElementById("orderAmount").value=totalCost
  }
