// constants

const EVEN_SITE_RATE = 80.0;
const ODD_SITE_RATE = 120.0;
const ALT_MEMBER_RATE = 5.0;
const WEEKLY_CLEANING_RATE = 50.0;
const VIDEO_SURVEILLANCE_RATE = 30.0;
const TAX_RATE = 0.15;
const STANDARD_RATE = 75.0;
const EXECUTIVE_RATE = 150.0;
const CANCELLATION_RATE = 0.6;

// inputs

const prompt = require("prompt-sync")();

const date = prompt("Enter the date (YYYY-MM-DD): ");
const site_number = parseInt(prompt("Enter the site number (1-100): "));
const member_name = prompt("Enter the member name: ");
const street_address = prompt("Enter the street address: ")
const city = prompt("Enter the city: ")
const province = prompt("Enter the province (NL, AB, QC): ").toUpperCase(); 
const postal_code = prompt("Enter the postal code (A1A1A1): ").toUpperCase();
const phone_num_home = prompt("Enter home phoner number (1234567890): ");
const phone_num_cell = prompt("Enter cell phoner number (1234567890): ");
const membership_type = prompt("Enter membership type ('S' = Standard, 'E' = Executive): ").toUpperCase();
const num_alt_members = parseInt(prompt("Enter number of alternate members: "));
const weekly_site_cleaning = prompt("Weekly site cleaning? (Y/N): ").toUpperCase();
const video_surveillance = prompt("Video surveilance? (Y/N): ").toUpperCase();

// calculations

let site_charges;
if (site_number % 2 === 0) {site_charges = EVEN_SITE_RATE + (num_alt_members * ALT_MEMBER_RATE);}
else {site_charges = ODD_SITE_RATE + (num_alt_members * ALT_MEMBER_RATE);};

let extra_charges;
if (weekly_site_cleaning === "Y" && video_surveillance === "Y") {extra_charges = WEEKLY_CLEANING_RATE + VIDEO_SURVEILLANCE_RATE;}
else if (weekly_site_cleaning === "Y" && video_surveillance === "N") {extra_charges = WEEKLY_CLEANING_RATE;}
else if (weekly_site_cleaning === "N" && video_surveillance === "Y") {extra_charges = VIDEO_SURVEILLANCE_RATE;}
else {extra_charges = 0};

const subtotal = site_charges + extra_charges;
const tax = subtotal * TAX_RATE;
const total_monthly_charge = subtotal + tax;

let monthly_dues;
if (membership_type === "E") {monthly_dues = EXECUTIVE_RATE;}
else {monthly_dues = STANDARD_RATE;};

const monthly_total_fees = total_monthly_charge + total_monthly_charge;
const total_yearly_fees = total_monthly_fees * 12;
const processing_fee = 58.99 / 12;
const monthly_payment = total_yearly_fees / 12 + processing_fee;
const cancellation_fee = total_yearly_fees * CANCELLATION_RATE;

// display

console.log();
console.log("       St. John's Marina & Yacht Club");
console.log("           Yearly Member Receipt");
console.log();
console.log("----------------------------------");
console.log();
console.log(" Client name and address: ");
console.log();
console.log(` ${member_name}`);
console.log(` ${street_address}`);
console.log(` ${city}, ${province}, ${postal_code}`);
console.log();
console.log(` phone: ${phone_num_home} (H)`);
console.log(`        ${phone_num_cell} (C)`);
console.log();
console.log(` Site #: ${site_number} Member type: ${membership_type}`);
console.log();
console.log(` Alternate members:                ${num_alt_members}`);

const site_cleaning_yes = "Yes";
const site_cleaning_no = "no";
const video_surveillance_yes = "Yes";
const video_surveillance_no = "No";

if (weekly_site_cleaning === "Y") {console.log(` Weekly site cleaning:            ${site_cleaning_yes}`)}
else {console.log(` Weekly site cleaning:            ${site_cleaning_no}`)};

if (video_surveillance === "Y") {console.log(` Video_Surveillance:                ${video_surveillance_yes}`)}
else {console.log(` Video_Surveillance:              ${video_surveillance_no}`)};

console.log();
console.log(` Site charges:                  $${site_charges.toFixed(2)}`);
console.log(` Extra charges:                  $${extra_charges.toFixed(2)}`);
console.log("                                  -----------");
console.log();
console.log(` Subtotal:                      $${subtotal.toFixed(2)}`);
console.log(` Sales tax (HST):                $${tax.toFixed(2)}`);
console.log("                                  -----------");
console.log(` Total monthly charges:         $${total_monthly_charge.toFixed(2)}`);
console.log(` Monthly dues:                   $${monthly_dues.toFixed(2)}`);
console.log("                                  -----------");
console.log(` Total monthly fees:            $${monthly_total_fees.toFixed(2)}`);
console.log(` Total yearly fees:            $${total_yearly_fees.toFixed(2)}`);
console.log();
console.log(` Monthly payment:               $${monthly_payment.toFixed(2)}`);
console.log();
console.log("----------------------------------");
console.log();
console.log(` Issued: ${date}`);
console.log(" HST reg no: 548-33-5849-4720-9885");
console.log();
console.log(` Cancellation fee:              $${cancellation_fee.toFixed(2)}`);
console.log();