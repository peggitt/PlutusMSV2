var DataTypes= null;
var ComboTypes= null;
var cellNumber=0;
var rowNumber =0;

jQuery( window ).load( function() {
    var $table1 = jQuery( "#table-2" );

        var $table1 = jQuery( '#table-2' );
        
        // Initialize DataTable
        $table1.DataTable( {
            "aLengthMenu": [[-1], ["All"]],
            "bStateSave": true
        });
        
        


    PopulateGrid();
} );




function PopulateGrid()
{

    var table = document.getElementById('table-2');
    
	var csrf = GetInputValue("hdncsrf");
	var mFormId = GetInputValue("hdnId");

	jQuery.ajax({
		type : "POST",
		url: "/ModuleConfig/"+mFormId+"/",
		data: {
			FormId: mFormId,
			QuestionId: 0,
			ActionID: "viewForm",
			csrfmiddlewaretoken: csrf,
			dataType: "json",
		
        },
            success: function(response)
            {
                if(response!=="[]" && response!=="")
                {
    
                    var jSonSession= response.returnDetails;

                    DataTypes= response.returnFormConrols;

                    if(jSonSession!=="")
                    {
                        
                        for (var j = 0; j < response.returnDetails.length; j++) {
                            var numRows = table.rows.length;
                            var NewnumRows = numRows;
                            var defaultDisable=false;
                            // Create a new row
                            var newRow = document.createElement('tr');

                            // Create and append new cell elements to the row
                            const cell0 = document.createElement('td');
                            const cell1 = document.createElement('td');
                            const cell6 = document.createElement('td');
                            const cell8 = document.createElement('td');
                            const cell12 = document.createElement('td');
                            const cell13 = document.createElement('td');
                            const cell14 = document.createElement('td');
                            const cell15 = document.createElement('td');

                            cell0.textContent = response.returnDetails[j].columnname;
                            cell1.textContent = response.returnDetails[j].columntype;
                            cell13.textContent = response.returnDetails[j].questionorder;
                            cell13.setAttribute('contenteditable', 'true');

                            cell14.textContent = response.returnDetails[j].searchprocedure;
                            cell14.setAttribute('contenteditable', 'true');

                            //cell1.setAttribute('contenteditable', 'true');
                            cell6.textContent = response.returnDetails[j].questioncaption;;
                            cell6.setAttribute('contenteditable', 'true');
                            cell8.textContent = response.returnDetails[j].gridorder;;
                            cell8.setAttribute('contenteditable', 'true');
                            cell12.textContent = response.returnDetails[j].functionevent;;
                            cell12.setAttribute('contenteditable', 'true');

                            var checkboxCell = document.createElement('td');
                            var checkboxInput = document.createElement('input');
                            checkboxInput.setAttribute('type', 'checkbox');
                            checkboxInput.id='Mandatory'+String(response.returnDetails[j].columnname);
                            checkboxInput.checked=response.returnDetails[j].ismandatory;
                            checkboxCell.appendChild(checkboxInput);  
                            
                            
                            var checkboxCell2 = document.createElement('td');
                            var checkboxInput2 = document.createElement('input');
                            checkboxInput2.setAttribute('type', 'checkbox');
                            checkboxInput2.id='GridItem'+String(response.returnDetails[j].columnname);
                            checkboxInput2.checked=response.returnDetails[j].isgriditem;
                            checkboxCell2.appendChild(checkboxInput2);  

                            var checkboxCell3 = document.createElement('td');
                            var checkboxInput3 = document.createElement('input');
                            checkboxInput3.setAttribute('type', 'checkbox');
                            checkboxInput3.id='SearchField'+String(response.returnDetails[j].columnname);
                            checkboxInput3.checked=response.returnDetails[j].issearchitem;
                            checkboxCell3.appendChild(checkboxInput3);  

                            var checkboxCell4 = document.createElement('td');
                            var checkboxInput4 = document.createElement('input');
                            checkboxInput4.setAttribute('type', 'checkbox');
                            checkboxInput4.id='UniqueField'+String(response.returnDetails[j].columnname);
                            checkboxInput4.checked=response.returnDetails[j].isunique;
                            checkboxCell4.appendChild(checkboxInput4);  
                            
                            var checkboxCell5 = document.createElement('td');
                            var checkboxInput5 = document.createElement('input');
                            checkboxInput5.setAttribute('type', 'checkbox');
                            checkboxInput5.id='AutoField'+String(response.returnDetails[j].columnname);
                            checkboxInput5.checked=response.returnDetails[j].isautofield;
                            checkboxCell5.appendChild(checkboxInput5); 

                            var checkboxCell6 = document.createElement('td');
                            var checkboxInput6 = document.createElement('input');
                            checkboxInput6.setAttribute('type', 'checkbox');
                            checkboxInput6.id='isLocked'+String(response.returnDetails[j].columnname);
                            checkboxInput6.checked=response.returnDetails[j].islocked;
                            checkboxCell6.appendChild(checkboxInput6); 

                            cell15.textContent = response.returnDetails[j].controltype;;
                            cell15.setAttribute('contenteditable', 'true');
                            //newRow.appendChild(comboboxCell1);
                            //checkboxInput7.checked=response.returnDeidtails[j].ControlType;
                            //checkboxCell7.appendChild(comboboxSelect1); 

                            newRow.appendChild(cell0);
                            newRow.appendChild(cell1);
                           // newRow.appendChild(comboboxCell1);
                           // newRow.appendChild(comboboxCell2);
                           // newRow.appendChild(comboboxCell3);
                            newRow.appendChild(checkboxCell);
                            newRow.appendChild(cell6);
                            newRow.appendChild(cell13);
                            newRow.appendChild(checkboxCell2);
                            newRow.appendChild(cell8);
                            newRow.appendChild(checkboxCell3);
                            newRow.appendChild(cell14);
                            newRow.appendChild(checkboxCell4);
                            newRow.appendChild(checkboxCell5);
                            newRow.appendChild(cell12);
                            newRow.appendChild(checkboxCell6);
                            newRow.appendChild(cell15);

                            // Append the new row to the table
                            jQuery('#table-2').dataTable().fnAddData( newRow );
                            //replaceCheckboxes(); // because there is checkbox, replace it
                            //giCount++;

                            //table.appendChild(newRow);

                            const cells = table.querySelectorAll('td');

                            // Add a click event listener to each cell
                            cells.forEach(function(cell, index) {
                                cell.addEventListener('click', function(event) {
                                // Get the cell number (column index)
                                cellNumber = index % 14 + 1; // Assuming 9 columns per row
                                // Calculate the row number (row index)
                                rowNumber = Math.floor(index / 14) + 1; // Assuming 3 columns per row

                                console.log(`Clicked on cell ${cellNumber} in row ${rowNumber}`);

                                console.log('Cell value changed:', this.textContent);
                                });

                                cell.addEventListener('keydown', function(event) {
                                    if (event.key === 'Backspace') {
                                    // Prevent the default Backspace behavior (browser navigation)
                                    event.preventDefault();
                                    
                                    // Optionally, you can add your own Backspace handling logic here
                                    // For example, clear the cell content when Backspace is pressed
                                    cell.textContent = '';
                                    }
                                });

                            });
                        }                     
                    }

                    var $table2 = jQuery("#table-2");
                    $table2.DataTable().draw(false); 
                    
                }else
                {
                    LoadCollabInfo(request.responseText);
                  //  LoadCollabSuccess("Proceed to Add New!");
                }
            },
            error: function (request, status, error) {
                LoadCollabInfo(request.responseText);
              //  LoadCollabSuccess("Proceed to Add New!");
            }
        });
}


function btnUpdateForm()
{
    const table = document.getElementById('table-2');

    // Initialize an array to hold the data
    const data = [];

    // Loop through each row in the table
    for (let i = 1; i < table.rows.length; i++) { // Start from 1 to skip the header row
    const row = table.rows[i];
    var rowColumn = row.cells[0].textContent;
    
    var MandatoryId = document.getElementById("Mandatory"+rowColumn);
    var MandatoryIdVal = MandatoryId.checked;

    var GridItemId = document.getElementById("GridItem"+rowColumn);
    var GridItemIdVal = GridItemId.checked;

    var SearchFieldId = document.getElementById("SearchField"+rowColumn);
    var SearchFieldIdVal = SearchFieldId.checked;

    var UniqueFieldId = document.getElementById("UniqueField"+rowColumn);
    var UniqueFieldIdVal = UniqueFieldId.checked;

    var AutoFieldId = document.getElementById("AutoField"+rowColumn);
    var AutoFieldIdVal = AutoFieldId.checked;

    var isLockedId = document.getElementById("isLocked"+rowColumn);
    var isLockedIdVal = isLockedId.checked;

  

    const rowData = {
        ColumnName: row.cells[0].textContent,
        ColumnType: row.cells[1].textContent,
        isMandatory: MandatoryIdVal,
        QuestionCaption: row.cells[3].textContent,
        QuestionOrder: row.cells[4].textContent,
        isGridItem: GridItemIdVal,
        GridOrder: row.cells[6].textContent,
        isSearchItem: SearchFieldIdVal,
        SearchProcedure: row.cells[8].textContent,
        isUnique: UniqueFieldIdVal,
        isAutoField: AutoFieldIdVal,
        FunctionEvent: row.cells[11].textContent,
        isLocked: isLockedIdVal,
        ControlType: row.cells[13].textContent,
    };

    // Add the object to the data array
    data.push(rowData);
    }

    // Convert the data array to a JSON string
    const jsonString = JSON.stringify(data);

    // Log the JSON string to the console
    console.log(jsonString);

    var mFormId = GetInputValue("hdnId");
    var csrf = GetInputValue("hdncsrf");

    $.ajax({
    type : "POST",
    url: "/ModuleConfig/"+mFormId+"/",
    data: {
        FormId: mFormId,
        SelectedSettings: jsonString,
		ActionID : "UpdateFormConfig",
		csrfmiddlewaretoken: csrf,
		dataType : "json",
		},
        success: function(response) {
        if(response!=="[]" && response!=="") {
            var jSonSessionData= response.returnDetails;
            LoadCollabSuccess('Information updated successfully!');
        }else {
            LoadCollabSuccess('Information updated successfully!');
            }
        },
            error: function (request, status, error) {
            LoadCollabError(request.responseText);
        }
    });

}
