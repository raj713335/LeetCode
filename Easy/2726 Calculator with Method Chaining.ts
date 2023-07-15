# https://leetcode.com/problems/calculator-with-method-chaining/description/

class Calculator {
    
  constructor(private  value : number) {
            this.value = value

  }
    
  add(value : number) : Calculator {
            this.value += value
            return this

  }
    
  subtract(value : number) : Calculator {
            this.value -= value
            return this

  }
    
  multiply(value : number) : Calculator {
            this.value *= value
            return this

  }

  divide(value : number) : Calculator {
            if(value !== 0){
                  this.value /= value
                  return this
            }else{
                  throw new Error("Division by zero is not allowed")
            }
  }
    
  power(value : number) : Calculator {
            this.value = this.value ** value
            return this
  }

  getResult() : number {
            return this.value
   
  }
}
