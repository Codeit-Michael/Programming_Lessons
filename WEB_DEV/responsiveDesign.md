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