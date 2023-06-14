function doGet() {
  var template = HtmlService.createTemplateFromFile('index.html');

  return template
    //.addMetaTag('viewport', 'width=device-width, initial-scale=1')
    .evaluate()
    .setSandboxMode(HtmlService.SandboxMode.IFRAME);
}

function getData() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Sheet1');
  const datarange = sheet.getRange("A1").getDataRegion();
  const data = datarange.getDisplayValues();

  const headers = data.shift();
  const userEmail = Session.getActiveUser().getEmail(); // Get the email of the user accessing the script
  const jsData = data
    .map((r) => {
      const tempObject = {};
      headers.forEach((header, i) => {
        tempObject[header] = r[i];
      });
      return tempObject;
    })
    .filter((item) => item["Mail ID"].trim() === userEmail); // Filter the data based on the user's email ID

  console.log(jsData);
  return jsData;
}


