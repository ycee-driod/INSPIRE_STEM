// Data Types:
/*  //Multiline Comment in JAVASCRIPT
1. Strings
2. Integers/Number
3. Booleans
4. Arrays
5. Objects

*/
let name = "Barney"
let height = 50
 function submit(){
    var input = document.getElementById("inputField").value;
    var input = parseInt(input);  //Data Type Conversion
    var input = input + 1;
    console.log(input)
 }

let adult = true;  //Boolean Data type
let fruits = ['peach', 'guava', 'orange',30, false] //Array of s list
let person = {
    Firstname: 'Ada',
    Lastname: 'Lovelace',
    age:'18',
    address: {
        country: 'Sudan',
        city: 'Khartoum',
        street: 'Bani',
 },
 children:['Khelly', 'Barnes']

}

console.log(typeof(fruits[4]))
console.log(typeof(person))

function saveItem(){
    var input = document.getElementById("inputField").value
    localStorage.setItem('inputItem', item);
    showWelcomeMessage(input)
}

function showWelcomeMessage(input){
    var messageElement = document.getElementById("showMessage")
    messageElement.textContent="We have saved your input as"+ input
}

var sroredItem = localstorage.getItem('inputItem');
if(storedItem)
