# UPC, QR, and SKU Codes: An Introduction to Product Identification

## Learning objectives

By the end of this tutorial, you should be able to:

* Explain what UPC, QR, and SKU mean and how they differ.
* Describe how scanning connects physical objects to information systems.
* Verify a UPC-A check digit.
* Plan and test a QR code safely.
* Design SKUs for a small inventory.

## 1. The big idea: identifiers versus data carriers

Imagine buying a blue, medium-sized T-shirt. The store needs to identify the product, find its price, update stock, and perhaps give you a link to washing instructions.

These tasks use two related concepts:

* An **identifier** is a value used to identify something in a system, such as a product number.
* A **data carrier** is a machine-readable representation of data, such as a printed barcode or QR symbol.

UPC is a standardized product-identification system commonly represented with a one-dimensional barcode. A SKU is a business's internal inventory identifier. A QR code is a two-dimensional data carrier that can encode a URL, text, or other data. They are not three interchangeable names for the same thing.

| Feature | UPC | QR code | SKU |
|---------|-----|---------|-----|
| Full name | Universal Product Code | Quick Response code | Stock Keeping Unit |
| Main purpose | Identify a trade item across participating businesses | Carry data for a scanner or camera to decode | Identify an inventory item within a business |
| Typical appearance | Vertical bars with digits underneath | Square grid of dark and light modules, usually with three large corner markers | Letters and numbers, often printed as text |
| Typical data | UPC-A carries a 12-digit GTIN-12 | A URL, text, contact details, or another supported payload | A business-defined value such as `TSH-BLU-M` |
| Who assigns the identifier or content? | Brand owner using GS1 allocation rules | Whoever creates the payload; a URL's owner controls its destination | The business managing the inventory |
| Common use | Retail checkout | Product information, tickets, menus, and links | Stock tracking, picking, and replenishment |

**Important:** A SKU can be encoded in a barcode such as Code 128 or in a QR code. That does not turn it into a UPC.

## 2. UPC: identifying retail products

### What is a UPC?

A UPC identifies a particular trade item, such as one size and color of a packaged product. Different variants or packaging levels may require different identifiers under GS1 rules. Individual units of the same trade item usually share the same UPC; it is not normally a serial number for each physical unit.

The most familiar format, **UPC-A**, has 12 digits:

* The first 11 digits contain the identification data.
* The final digit is a calculated **check digit**.

GTIN means **Global Trade Item Number**. The 12-digit number represented by UPC-A is a GTIN-12. UPC-E is a compact representation of certain eligible UPC numbers; this lesson's examples use UPC-A.

GS1 Company Prefix lengths vary, so do not assume that every UPC splits into a fixed number of manufacturer and product digits. A UPC also does not reliably tell you where an item was manufactured.

### What happens at checkout?

1. The scanner reads the bars and spaces and decodes the number.
2. The point-of-sale application looks up that number in its product database.
3. The database supplies the description, current price, and tax rules.
4. When the sale completes, the inventory system records the stock change.

The UPC itself normally does **not** contain the current selling price, stock quantity, or full product description. Different stores can charge different prices for the same UPC because those values live in their databases.

### Tutorial: calculate a UPC-A check digit

Use the sample number `036000291452` for this exercise only. It is not an identifier you should assign to your own product.

Start with the first 11 digits: `03600029145`. Count positions from the left, starting at 1.

| Step | Calculation | Result |
|------|-------------|--------|
| Add digits in odd positions (1, 3, 5, 7, 9, 11) | 0 + 6 + 0 + 2 + 1 + 5 | 14 |
| Multiply that sum by 3 | 14 x 3 | 42 |
| Add digits in even positions (2, 4, 6, 8, 10) | 3 + 0 + 0 + 9 + 4 | 16 |
| Add the weighted sums | 42 + 16 | 58 |
| Find the digit needed to reach the next multiple of 10 | 58 + 2 = 60 | **2** |

The formula is `check digit = (10 - (weighted sum mod 10)) mod 10`. If the weighted sum already ends in zero, the check digit is zero.

The final digit in `036000291452` is 2, so the number passes this check.

**Try it:** Would `036000291453` pass? No: its final digit should be 2, not 3.

A valid check digit detects many data-entry errors, but does not prove that a number is legitimately assigned or that a product is authentic. For real products, obtain identifiers through GS1 and follow its allocation rules rather than inventing random UPCs.

## 3. QR codes: carrying information in two dimensions

### How does a QR code work?

A QR code uses a grid of small squares called **modules**. Its position-detection patterns help a reader locate and orient it. Error correction can recover data from some damage, depending on the selected level and the damage pattern; it does not make every damaged code readable.

A QR code can contain:

* A web address, such as `https://example.com/`.
* Plain text, such as `Intro to IT practice`.
* Structured data, such as contact or Wi-Fi configuration details, if the scanning application supports that format.

The information is encoded in the symbol. The scanner decodes it, and an application decides what to do next. Reading plain text can work without internet access; opening an online destination usually requires a network connection.

### Static versus dynamic QR codes

* A **static QR code** directly encodes its payload. Changing the encoded text or URL requires a new symbol. The content of a web page at that URL can still change.
* A service marketed as a **dynamic QR code** usually encodes a redirect URL. The service can change where that URL sends visitors without changing the printed symbol.

The printed symbol itself does not update. Redirect services add dependencies, may track scans, and can stop working if the account expires or the service closes.

### Tutorial: create and test a practice QR code

1. Choose a trusted QR generator, preferably one that can generate locally without uploading your data. No paid dynamic-code subscription is needed for this exercise.
2. Select plain text and enter `Intro to IT practice`. Do not enter passwords, personal information, or access tokens.
3. Generate the symbol with dark modules on a light background. Preserve the blank **quiet zone** of at least four modules around a standard QR symbol.
4. Save or print it without stretching, cropping, or covering the corner patterns.
5. Use your phone camera or a trusted QR reader to scan it. Confirm that the decoded text exactly matches `Intro to IT practice`.
6. Create a second code containing `https://example.com/`. Preview the decoded URL before opening it, then confirm that the browser reaches the expected domain.
7. Test the final printed size on another device and under normal lighting. If it fails, increase its size, improve contrast, reduce payload length, and check the quiet zone.

**Expected result:** The first code displays the practice text; the second offers the example website. You are testing both successful decoding and correct content, not just whether a camera recognizes a square.

### QR scanning safety

A QR code hides its contents from casual visual inspection. Attackers can place replacement stickers over legitimate codes or send codes that lead to phishing sites.

* Preview the destination and check the actual domain before opening it.
* Do not install an app or enter credentials merely because a code asks you to.
* For payments, verify the recipient and amount independently.
* Treat decoded content as untrusted input. Scanning is not proof of authenticity.
* Remember that anyone who can photograph a printed code can read its payload.

## 4. SKU: organizing inventory inside a business

### What is a SKU?

A **Stock Keeping Unit** is an internal identifier used to distinguish inventory items. A store might use `TSH-BLU-M` for a blue, medium T-shirt.

Unlike a UPC, there is no universal SKU format or shared global meaning. Two businesses may use different SKUs for the same product, or accidentally use the same SKU for unrelated products. An ordinary SKU also has no mandatory check digit.

### Tutorial: design a small SKU system

Suppose a shop sells T-shirts in two colors and two sizes. Define the pattern:

`CATEGORY-COLOR-SIZE`

| Product variant | SKU | Quantity on hand |
|-----------------|-----|------------------|
| T-shirt, blue, medium | `TSH-BLU-M` | 12 |
| T-shirt, blue, large | `TSH-BLU-L` | 8 |
| T-shirt, red, medium | `TSH-RED-M` | 10 |
| T-shirt, red, large | `TSH-RED-L` | 6 |

1. Write down allowed category, color, and size abbreviations.
2. Assign a unique SKU to each variant you track separately.
3. Check for duplicates before importing the inventory.
4. Keep identifiers stable; do not include changing values such as price or stock count.
5. Avoid ambiguous characters where possible, such as uppercase O versus zero.
6. Store identifiers as text in spreadsheets and databases so leading zeros are preserved. This is especially important for UPCs.
7. If you need scannable labels, encode the SKU with a suitable barcode format or QR code and verify what your scanner returns.

An internal-only product may have a SKU without a UPC. A retailer selling a branded product may store both the supplier's UPC and its own SKU.

## 5. Connecting all three in an information system

The following is a simplified database record for one hypothetical product. The sample UPC is for demonstration only.

| Field | Example | Purpose |
|-------|---------|---------|
| Internal SKU | `TSH-BLU-M` | Store's inventory key |
| UPC / GTIN-12 | `036000291452` | External product identifier for lookup |
| Description | Blue T-shirt, medium | Human-readable product information |
| Price | USD 19.99 | Store-controlled selling price |
| Quantity on hand | 12 | Current inventory balance |
| QR payload | `https://example.com/` | Example link to product information |

A customer scans the QR code to open information. A cashier scans the UPC to look up the product. A stockroom worker uses the SKU to pick the correct variant.

For this exercise, selling two blue, medium T-shirts changes the quantity from **12 to 10**. The SKU and UPC stay the same; the stock quantity changes in the database, not in the printed codes.

Real inventory systems may map several external identifiers to one internal item and manage stock by location. A QR code links to this record only if the application or destination page is designed to make that connection.

## 6. Practice and review

### Hands-on assignment

1. Make a spreadsheet for three imaginary products with columns for SKU, description, price, and quantity.
2. Give each product a unique SKU and explain your naming convention.
3. Add a UPC column formatted as text. Use the sample above for one demonstration row only; leave the others blank rather than claiming invented identifiers are assigned UPCs.
4. Generate a QR code containing one of your SKUs as plain text. Scan it and verify the exact value.
5. Record a sale of two units and update the quantity without changing the identifiers.
6. Explain which application would be needed to turn the scanned SKU into a product lookup.

### Knowledge check

1. Does a UPC normally contain the store's current price?
2. Does a QR code always require an internet connection to decode?
3. Must two stores use the same SKU for the same product?
4. Does a valid UPC check digit prove that a product is genuine?
5. Does putting a SKU in a QR code automatically connect it to an inventory database?

**Answers:** 1. No; the price is usually retrieved from a database. 2. No; decoding is local, though visiting an online URL needs connectivity. 3. No; SKUs are internal. 4. No; the check digit is an error-detection mechanism. 5. No; software must implement the lookup.

## Further reading

* [GS1: UPC and EAN barcodes](https://www.gs1.org/standards/barcodes/ean-upc)
* [GS1: Check digit calculator](https://www.gs1.org/services/check-digit-calculator)
* [DENSO WAVE: What is a QR code?](https://www.qrcode.com/en/about/)
* [DENSO WAVE: QR code error correction](https://www.qrcode.com/en/about/error_correction.html)
