//TODO filters for style and size

//TODO only show toppings when pizza with toppings selected

document.addEventListener("DOMContentLoaded", event => {
  if (document.querySelector("#pizza-form")) {
    document.querySelector("#pizza-form").addEventListener("submit", function (event) {
      event.preventDefault()
      let selectedIndex = document.querySelector("#select-pizza").selectedIndex
      let selected = document.querySelector("#select-pizza")[selectedIndex].value
      //size-style-description-price(cents)
      let options = selected.split("-")
      // let form = document.createElement("form")
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
      // form.method = "post"
      // form.action = "orders/pizza/add"
      // document.querySelector("body").appendChild(form)
      console.log(size, style, price, description)
      this.submit()
    })
  }

})