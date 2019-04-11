
function getToppings(form, description) {
  let toppings = []
  let toppingsCount = 0
  // document.querySelectorAll("form#pizza-form .toppings-check input")[0].checked

  let ingredients = form.querySelectorAll(".toppings-check input")
  if (description.indexOf("1") > -1) toppingsCount = 1
  else if (description.indexOf("2") > -1) toppingsCount = 2
  else if (description.indexOf("3") > -1) toppingsCount = 3
  let counter = 0
  for (let i = 0; i <= ingredients.length; i++) {
    if (counter >= toppingsCount) break //quit if all toppings found
    if (ingredients[i].checked) {
      toppings.push(ingredients[i].value)
      counter++;
    }
  }
  return toppings.join(',')
}

document.addEventListener("DOMContentLoaded", event => {
  
  if (document.querySelector("#pizza-form")) {
    document.querySelector(".toppings-check").style.display = "none"
    document.querySelector("#select-pizza").addEventListener("change",function(event){
      if (this[this.selectedIndex].value.indexOf("topping") > -1){
        document.querySelector(".toppings-check").style.display = "block"
      } else {
        document.querySelector(".toppings-check").style.display = "none"
      }
    })
    document.querySelector("#pizza-form").addEventListener("submit", function (event) {
      event.preventDefault()
      let selectedIndex = document.querySelector("#select-pizza").selectedIndex
      let selected = document.querySelector("#select-pizza")[selectedIndex].value
      //size-style-description-price(cents)
      let options = selected.split("-")
      let size = document.createElement("input")
      size.name = "size"
      size.value = options[0]
      let style = document.createElement("input")
      style.name = "style"
      style.value = options[1]
      let description = document.createElement("input")
      description.name = "description"
      description.value = options[2]
      price = document.createElement("input")
      price.value = options[3]
      price.name = "price"

      this.appendChild(size)
      this.appendChild(style)
      this.appendChild(description)
      this.appendChild(price)
      //pick up toppings
      //pass in the form and the description and get back comma separated list of 1,2, or 3 toppings
      let toppingsValue = getToppings(this, options[2])
      let toppings = document.createElement("input")
      toppings.name = "toppings"
      toppings.value = toppingsValue
      this.appendChild(toppings)

      // console.log(size, style, price, description, toppings)
      this.submit()
    })
  }

})