module.exports = function(name, age) {
    console.log("Hello !!")
    return {
        get_name: function() {return name},
        get_age: function() {return age}
    }
}