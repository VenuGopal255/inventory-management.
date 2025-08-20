// JS- it is used for mainly in web development and it is used to check the data is valid or not to show before response

/* 
DATA types:
    1.number(int,float)
    2.str
    3.bool
    4.symbol(===)
    5.object(arrey,obj,null)
    6.undefine

OPERATORS:
    1.arthmetic
    2.unary- (pre increment,post inc/dec) 
    3.bitwise
    4.swith
    5.nulish colise
    6.operational chaining
    7.logical
    8.assignment
   */

    /*let x;
    x=[10,20,'gopi',true,'python']
    x.push(100)
    console.log(x)

    //slicing
    let res=x.slice(1,4)
    console.log(res)*/

    //condtional statements 
    // ex:1
    let x;
    x=parseInt(prompt('enter no:'));
    if (x%2 ==0){
        console.log('even');
    }
    else{
        console.log('odd');
    }

    // ex 2:
    let marks;
    marks=parseInt(prompt('enter no:'));
    if (marks>80)
        console.log('a+');
    else if(marks>70)
        console.log('a');
    else if(marks>60)
        console.log('b');
    else
        console.log('c');