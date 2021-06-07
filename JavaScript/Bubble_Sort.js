// Bubble Sort - 

// Swaping Function -
function swap(){
    var Temp = arrToSort[First_Element];
    arrToSort[First_Element] = arrToSort[Adjacent_Element];
    arrToSort[Adjacent_Element] = arrToSort[First_Element];
}

// Bubble Sort Function -
function bubbleSort(arrToSort){
    // 2 loops -
    // First loop takes First_Element
    for (let First_Element = 0; First_Element < arrToSort.lenght; First_Element++){
        // Second loop takes Adjacent_Element (i.e Next Element) -
        for(let Adjacent_Element = 0; Adjacent_Element < arrToSort.lenght; Adjacent_Element++){
            // Check If First_Element is < than Adjacent_Element 
            // If Yes than swap those values -
            swap(arrToSort[First_Element], arrToSort[Adjacent_Element], arrToSort)
        }
    } 
    // return Sorted Array -
    return arrToSort
}


// Take Array To Sort -
var arrToSort = [2, 5, 0, 1, 7, 5];

// Show User Sorted Array -
console.log(bubbleSort(arrToSort));
