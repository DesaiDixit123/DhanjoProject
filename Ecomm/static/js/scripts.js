function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function () {
        var output = document.getElementById('profileImagePreview');
        output.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
}


document.addEventListener("DOMContentLoaded", function () {
 
    const productCards = document.querySelectorAll('.card');

    productCards.forEach(card => {
      const productTitleElement=card.querySelector(".product-title")
      if(productTitleElement){
        const titleText=productTitleElement.textContent.trim()
        const words=titleText.split(' ')
        if(words.length >5 ){
          const trunctedTitle=words.slice(0,5).join(' ')+'...'
          productTitleElement.textContent=trunctedTitle
        }
      }

      const productDescriptionElement=card.querySelector(".product-description")
      if(productDescriptionElement){
        const descriptionText=productDescriptionElement.textContent.trim()
        const descriptionWords=descriptionText.split(' ')
        if(descriptionText.length > 10){
          const trunctedDescription=descriptionWords.slice(0,10).join(' ')+'...'
          productDescriptionElement.textContent=trunctedDescription
        }
      }
     
      const originalPriceElement = card.querySelector('.original-price');
      const discountPriceElement = card.querySelector('.discount-price');
      const discountPercentageElement = card.querySelector('.discount-percentage');

      function formatPrice(price) {
        return price.toLocaleString('en-IN');
      }

      if (originalPriceElement) {
        const originalPrice = parseFloat(originalPriceElement.textContent.trim());
        if (!isNaN(originalPrice)) {
          originalPriceElement.textContent = formatPrice(originalPrice);
        }
      }

      if (discountPriceElement) {
        const discountPrice = parseFloat(discountPriceElement.textContent.trim());
        if (!isNaN(discountPrice)) {
          discountPriceElement.textContent = formatPrice(discountPrice);
        }
      }
      if (originalPriceElement && discountPriceElement) {
       
        const originalPrice = parseFloat(originalPriceElement.textContent.replace(/,/g,''));
        const discountPrice = parseFloat(discountPriceElement.textContent.replace(/,/g,''));

        if (originalPrice > 0 && discountPrice > 0) {
          
          const discountPercentage = (((originalPrice - discountPrice) / originalPrice) * 100).toFixed(1);

         
          discountPercentageElement.textContent = `${discountPercentage}% Off`;
        }
      }
    });
  });