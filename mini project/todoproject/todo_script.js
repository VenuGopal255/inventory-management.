document.querySelector('#btn').addEventListener('click',additem);

function additem(){
    let items,list_item,un_list,edit_btn,del_btn;
    items=document.querySelector('#t1').value;
    list_item=document.createElement('li');
    un_list=document.querySelector('#items');
    edit_btn=document.createElement('button');   
    edit_btn.innerText='edit'
    edit_btn.style.marginLeft='5px';
    del_btn=document.createElement('button')    
    del_btn.innerText='delete'
    del_btn.style.marginLeft='5px';
    list_item.textContent=items;  
    list_item.appendChild(edit_btn);
    list_item.appendChild(del_btn); 
    un_list.appendChild(list_item);
    list_item.style.color='black';
    list_item.style.fontSize='large';
    del_btn.addEventListener('click',()=>{
        list_item.remove()
    });
    edit_btn.addEventListener('click',()=>{
        let newtext=prompt('edit item:',list_item.firstChild.textContent);
        if (newtext!==null && newtext.trim()!==""){
            list_item.firstChild.textContent=newtext;
        }
    });
}  
