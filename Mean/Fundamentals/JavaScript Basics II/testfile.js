function magic_multiply(x, y){
    //Test 1
    if(typeof(x)== "string" || typeof(y)== "string"){
        return "Error: Can not multiply by string";

    }else{
        if(Array.isArray(x) == true){
            for(i in x){
                x[i] = x[i]*y;
            }
        }
        else{
            x = x*y
        }
        return x;
    }
}

let test1 = magic_multiply(5, 2);
console.log(test1);

let test2 = magic_multiply(0, 0);
console.log(test2);

let test3 = magic_multiply([1, 2, 3], 2);
console.log(test3);

let test4 = magic_multiply(7, "three");
console.log(test4);