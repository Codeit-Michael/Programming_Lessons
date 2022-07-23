## HTML Extras
### Main Tag `<main></main>`
-HTML 5 has some elmnts HTML5 has some elmnts that identify diff. content areas, which is useful for SEO. Main tag contains the main subject of your page.
-Main tag should be placed after `h1` tag

### 'alt' attribute for img tag
-'img' tag codes looki like this typically:
```html
<img src='link'>
```
-But sometimes pages don't load as expected, so we have `alt` attribute incase image don't load, it tells what it contains
```html
<img src='link' alt='picture of myself'>
```

### Section tag `<section></section>`
-A tag like a container that separates the contents part to other content parts, inside `main` tag.

### Figure tag `<figure></figure>`
-self-contained content and will allow you to associate an image with a caption
-when adding caption to an element, pictures most of the time, use `figcation` tag. Always put it below the img
```html
<figure>
	<img src='link' alt='pic'>
	<figcaption>Never gonna give you up</figcaption>
</figure>
```
-To emphasize a word/phrase on a caption, use `em` tag 
```html
<figcaption>emphasize <em>me</em> okay</figcaption>
```
-`strong` tag, was just like 'bold' tag
-`label` tag associates the input on its label `<label><input type="radio"> Indoor</label>`

### Naming radio buttons
-Radio buttons used to be picked only 1 item in their choices. Once you select a choice different from what you selected first, it must remove the last selected and select what you recently clicked. To do this, name all of the 'radio' button the same.
-Also, always add `fieldset` tag that nests all of the choices fields.
-`legend` tag acts as a caption for the content in the fieldset element.
```html
<fieldset>
	<legend>What electric current do you prefer?</legend>
	<label><input name='AC/DC' id='ac' value='ac' type='radio'>AC</label>
	<label><input name='AC/DC' id='dc' value='ac' type='radio'>DC</label>
</fieldset>
```
-Aside using the order `<label><input></label>`, you can use `<input><label></label>` and to associate, just use `for` attribute with the same value as `input`'s id.
```html
<fieldset>
	<legend>What electric current do you prefer?</legend>
	<input name='AC/DC' id='ac' value='ac' type='radio'><label for='ac'>AC</label>
	<input name='AC/DC' id='dc' value='ac' type='radio'><label for='dc'>DC</label>
</fieldset>
```

### HTML file areas that souls be present
-`lang` attribute in HTML tag specifies what language do its contents have
-`<DOCTYPE html>` called the documentation type/DOCTYPE declaration is an instructions to the web browser about what version of HTML the page is written in.
-`<meta charset="UTF-8"` tells the browser to encode multiple languages

***

## CSS Basics
-`<section></section>` used when having  2 or more diff. sections
-CSS syntax:
```css
selector {property:value;}
``` 
-Importing CSS in HTML
```hmtl
<link rel="stylesheet" href="styleDIR.css"/>
```

### Responsive Site Design
-Design will be responsive depends on the device used to load it
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
```
-`<article></article>` elements commonly contain multiple elements that have related information
```html
  <article>
    <p>French Vanilla</p>
    <p>3.00</p>
  </article>
```
-To make things align on the same line:
```css
.item {
  display:inline-block;
}
```
-If you have `p` tags, it will bring the other one below. What you should do is delete all the whitespaces between them (in HTML file) and make them on the same line.
```html
<!-- instead of this -->
<p>Pumpkin Spice</p>
<p>3.50</p>

<!-- do this -->
<p>Pumpkin Spice</p><p>3.50</p>
```
-`padding` property in CSS gives space on your div, etc. depends on px or % you give.
-`max-width:500px;` controls the element to not be loose your designs on wide screens.

### FONT and FONT-FAMILY
-Typeface (aka font) means the design, font means the file containing the typeface, and font-family means collection of related fonts. 
```css
h1, h2 {
  font-family: Impact;
}
```
-You can add a fallback value for the font-family by adding another font name separated by a comma.
```css
h1, h2 {
  font-family: Impact, serif;
}
```
-Change the height of the hr element using `height` attribute.
```css
hr {
  height: 2px;
  background-color: brown;
  border-color: brown;
}
```
>> Note: the `border-width` has default value of 1px. If you give an `hr` a height of `2px`, then the total height value of hr is 4px (2px + top border-width px + bottom border-width px)

### Tag styling with conditions
```css
/* customed color */
a {
  color: black;
}

/* color that appears when already visited */
p:visited {
  color: grey;
}

/* color when hovered */
h1:hover {
  color: brown;
}

/* activated */
a:active {
  color: white;
}
```
-The browser having some default top margin for the h1 element. You can change the top margin of the h1 element to 0 to remove all the top margin.
```css
h1 {
  font-size: 40px;
  margin-top: 0;
}
```
### Centering an Image
```css
img {
  display:block; /* making it a 1-line element */
  margin-left:auto;
  margin-right:auto;
}
```

### Easier way of pulling item
-Use `-px` value for pulling your nodes on the place you want/
```css
img {
  display: block;
  margin-top: -25px;
```
