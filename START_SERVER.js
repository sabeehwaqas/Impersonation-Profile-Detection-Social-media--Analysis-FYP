const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');
const app = express();
const ejs = require('ejs');
const fs = require('fs');


app.use(bodyParser.urlencoded({ extended: true }));
//app.use(express.static(__dirname + '/Website/assets'));

app.get('/', (req, res) => {
    app.use(express.static(__dirname + '/Website/assets'));
    app.use(express.static(__dirname + '/Website'));
    res.sendFile(__dirname + '/Website/index1.html');
});

app.post('/submit-form', (req, res) => {
    app.use(express.static(__dirname + '/Website/assets'));
    app.use(express.static(__dirname + '/Website'));
    const { name } = req.body;
    const { depth } = req.body;
    //console.log(name);
    //console.log(depth);
    const pythonProcess = spawn('python', ['START_HERE.py', name,depth]);



    pythonProcess.on('close', (code) => {
        if (code !== 0){
            res.write("OOPS Error Occured In the Algorithm!!");
            res.end();
        };
        //console.log(`child process exited with code ${code}`);

        //res.send('Form data submitted successfully!');

        const { JSDOM } = require('jsdom');
        const { document } = (new JSDOM('')).window;
        const data = fs.readFileSync('dataofprediction.json');
        const profiles = JSON.parse(data);
        //const table = document.createElement('body');
        app.use(express.static(__dirname + '/Website/assets'));
        app.use(express.static(__dirname + '/Website'));
        app.use(express.static(__dirname + '/images'));
        var i;

        const page = `      
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js" defer></script>
</head>
<body>
    <h1>Results</h1>
${profiles.map((user) =>

                      `
<h1>${'Group'} </h1>
<div class="accordion">
  <div class="accordion-item">
<div class="accordion-item-header" >
    <div style="display: flex; align-items: center; gap: 1rem">
        <img src="glasses.jpg" alt="Profile Image" width="65" height="65">
        <div class="user_name">${user.Username}</div> 
    </div> 
    <div class="authenticity">
        <div class="">Real</div>      
    </div>
</div>
    <div class="accordion-item-body">
      <div class="accordion-item-body-content">
        <div style="width: 70%;float:left">
            <table class="styled-table">
                <thead>
                    <tr class="active-row">
                        <td class="value_taker">Screen name</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Tweeter ID</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Following</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Followers</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Description</td>
                        <td class="description">Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis eaque, a aspernatur reprehenderit aliquam iusto.</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Tweets Number</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Date joined</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Tweet_Number</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Verification_Status</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Birthday</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Fake followers</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Retweet ratio</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Spammer</td>
                        <td>5150</td>
                    </tr>
                    <!-- and so on... -->
                
                </tbody>
            </table>
       </div>
       <div style="width:80%">
        <button type="button" style="float:right" onclick="/details/${user.Username}">More Details!</button>
       </div>
      </div>
    </div>
</div>
  </div>
${user.List1.map((List)=>`
<div class="accordion">
  <div class="accordion-item">
<div class="accordion-item-header" >
    <div style="display: flex; align-items: center; gap: 1rem">
        <img src="glasses.jpg" alt="Profile Image" width="65" height="65">
        <div class="user_name">${List.Username}</div> 
    </div> 
    <div class="authenticity">
        <div class="">authenticity = 100%</div>      
    </div>
</div>
    <div class="accordion-item-body">
      <div class="accordion-item-body-content">
        <div style="width: 70%;float:left">
            <table class="styled-table">
                <thead>
                    <tr class="active-row">
                        <td class="value_taker">Screen name</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Tweeter ID</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Following</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Followers</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Description</td>
                        <td class="description">Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis eaque, a aspernatur reprehenderit aliquam iusto.</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Tweets Number</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Date joined</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Tweet_Number</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Verification_Status</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Birthday</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Fake followers</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Retweet ratio</td>
                        <td>5150</td>
                    </tr>
                    <tr class="active-row">
                        <td class="value_taker">Spammer</td>
                        <td>5150</td>
                    </tr>
                    <!-- and so on... -->
                
                </tbody>
            </table>
       </div>
       <div style="width:80%">
        <button type="button" style="float:right" onclick="alert('Hello world!')">Click Me!</button>
       </div>
      </div>
    </div>
  </div>
</div>

`).join('')
            };
        
`).join('')
            };                  

                            </body>
                        </html>`
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(page);
        //fs.writeFileSync('Results.html', page);
        res.end();
    });
});
//const nodemailer = require('nodemailer');

//let transporter = nodemailer.createTransport({
//    service: 'gmail',
//    auth: {
//        user: 'Flaseflag000@gmail.com',
//        pass: 'Student@123'
//    }
//});

//app.post('/form-Contact', (req, res) => {
    
//        // Get the form data from the request object
//        const name = req.body.name;
//        const email = req.body.email;
//        const message = req.body.message;

//        // Set up the email message
//        const mailOptions = {
//            from: 'your_email@gmail.com',
//            to: 'recipient_email@example.com',
//            subject: 'New feedback received',
//            text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}`
//        };

//        // Send the email
//        transporter.sendMail(mailOptions, (error, info) => {
//            if (error) {
//                console.log(error);
//                res.send('Error: ' + error);
//            } else {
//                console.log('Email sent: ' + info.response);
//                res.send('Email sent!');
//            }
//        });
//});

app.listen(8000, () => {
    console.log('Server Started!!')
});