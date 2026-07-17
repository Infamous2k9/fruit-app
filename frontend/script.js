fetch("http://127.0.0.1:8000/fruits/")
  .then((response) => response.json())
  .then((fruits) => {
    console.log(fruits);

    const list = document.getElementById("fruit-list");

    fruits.forEach((fruit) => {
      const li = document.createElement("li");

      li.textContent = `${fruit.name} - ${fruit.gewicht}g - ${fruit.farbe}`;

      list.appendChild(li);
    });
  })
  .catch((error) => {
    console.error(error);
  });
