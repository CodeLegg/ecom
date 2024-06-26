///////////////////////////////////////////////////////////////

// SLIDER

const initSlider = () => {
    const imageList = document.querySelector(".slider-wrapper .image-list");
    const slideButtons = document.querySelectorAll(
      ".slider-wrapper .slide-button"
    );
    const sliderScrollbar = document.querySelector(
      ".slider-container .slider-scrollbar"
    );
    const scrollbarThumb = sliderScrollbar.querySelector(".scrollbar-thumb");
    const maxScrollLeft = imageList.scrollWidth - imageList.clientWidth;
    const firstImage = imageList.firstElementChild;
    const computedStyle = getComputedStyle(imageList); // Get the computed style of the image list
    const imageWidth =
      firstImage.clientWidth + parseInt(computedStyle.gridColumnGap); // Include grid gap in image width
  
    scrollbarThumb.addEventListener("mousedown", (e) => {
      const startX = e.clientX;
      const thumbPosition = scrollbarThumb.offsetLeft;
  
      // Uodate thumb position on mouse move
      const handleMouseMove = (e) => {
        const deltaX = e.clientX - startX;
        const newThumbPosition = thumbPosition + deltaX;
        const maxThumbPosition =
          sliderScrollbar.getBoundingClientRect().width -
          scrollbarThumb.offsetWidth;
  
        const boundedPosition = Math.max(
          0,
          Math.min(maxThumbPosition, newThumbPosition)
        );
        const scrollPosition =
          (boundedPosition / maxThumbPosition) * maxScrollLeft;
  
        scrollbarThumb.style.left = `${boundedPosition}px`;
        imageList.scrollLeft = scrollPosition;
      };
      // remove event listener on mouse up
      const handleMouseUp = () => {
        document.removeEventListener("mousemove", handleMouseMove);
        document.removeEventListener("mouseup", handleMouseUp);
      };
      // add event listener for drag interaction
      document.addEventListener("mousemove", handleMouseMove);
      document.addEventListener("mouseup", handleMouseUp);
    });
  
    // Slide images according to the slide button clicks
    slideButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const direction = button.id === "prev-slide" ? -1 : 1;
        const scrollAmount = imageWidth * direction;
        imageList.scrollBy({ left: scrollAmount, behavior: "smooth" });
      });
    });
  
    const handleSlideButtons = () => {
      slideButtons[0].style.display =
        imageList.scrollLeft <= 0 ? "none" : "block";
      slideButtons[1].style.display =
        imageList.scrollLeft >= maxScrollLeft ? "none" : "block";
    };
  
    imageList.addEventListener("scroll", () => {
      handleSlideButtons();
      updateScrollThumbPosition(); // Update scrollbar thumb position when the slider is scrolled
    });
  
    const updateScrollThumbPosition = () => {
      const scrollPosition = imageList.scrollLeft;
      const thumbPosition =
        (scrollPosition / maxScrollLeft) *
        (sliderScrollbar.clientWidth - scrollbarThumb.offsetWidth);
      scrollbarThumb.style.left = `${thumbPosition}px`;
    };
  
    // Call handleSlideButtons initially to set initial button visibility
    handleSlideButtons();
    updateScrollThumbPosition();
  };
  
  window.addEventListener("load", initSlider);
  
  ///////////////////////////////////////////////////////////////////
  
  // SECOND SLIDER
  
  const initSecondSlider = () => {
    const secondImageList = document.querySelector(
      ".second-slider-wrapper .second-image-list"
    );
    const secondSlideButtons = document.querySelectorAll(
      ".second-slider-wrapper .second-slide-button"
    );
    const secondSliderScrollbar = document.querySelector(
      ".second-slider-container .second-slider-scrollbar"
    );
    const secondScrollbarThumb = secondSliderScrollbar.querySelector(
      ".second-scrollbar-thumb"
    );
    const secondMaxScrollLeft =
      secondImageList.scrollWidth - secondImageList.clientWidth;
    const secondFirstImage = secondImageList.firstElementChild;
    const secondComputedStyle = getComputedStyle(secondImageList);
    const secondImageWidth =
      secondFirstImage.clientWidth + parseInt(secondComputedStyle.gridColumnGap);
  
    secondScrollbarThumb.addEventListener("mousedown", (e) => {
      const startX = e.clientX;
      const thumbPosition = secondScrollbarThumb.offsetLeft;
  
      const handleMouseMove = (e) => {
        const deltaX = e.clientX - startX;
        const newThumbPosition = thumbPosition + deltaX;
        const maxThumbPosition =
          secondSliderScrollbar.getBoundingClientRect().width -
          secondScrollbarThumb.offsetWidth;
  
        const boundedPosition = Math.max(
          0,
          Math.min(maxThumbPosition, newThumbPosition)
        );
        const scrollPosition =
          (boundedPosition / maxThumbPosition) * secondMaxScrollLeft;
  
        secondScrollbarThumb.style.left = `${boundedPosition}px`;
        secondImageList.scrollLeft = scrollPosition;
      };
  
      const handleMouseUp = () => {
        document.removeEventListener("mousemove", handleMouseMove);
        document.removeEventListener("mouseup", handleMouseUp);
      };
  
      document.addEventListener("mousemove", handleMouseMove);
      document.addEventListener("mouseup", handleMouseUp);
    });
  
    secondSlideButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const direction = button.id === "prev-slide-second" ? -1 : 1;
        const scrollAmount = secondImageWidth * direction;
        secondImageList.scrollBy({ left: scrollAmount, behavior: "smooth" });
      });
    });
  
    const handleSecondSlideButtons = () => {
      secondSlideButtons[0].style.display =
        secondImageList.scrollLeft <= 0 ? "none" : "block";
      secondSlideButtons[1].style.display =
        secondImageList.scrollLeft >= secondMaxScrollLeft ? "none" : "block";
    };
  
    secondImageList.addEventListener("scroll", () => {
      handleSecondSlideButtons();
      updateSecondScrollThumbPosition();
    });
  
    const updateSecondScrollThumbPosition = () => {
      const scrollPosition = secondImageList.scrollLeft;
      const thumbPosition =
        (scrollPosition / secondMaxScrollLeft) *
        (secondSliderScrollbar.clientWidth - secondScrollbarThumb.offsetWidth);
      secondScrollbarThumb.style.left = `${thumbPosition}px`;
    };
  
    handleSecondSlideButtons();
    updateSecondScrollThumbPosition();
  };
  
  window.addEventListener("load", initSecondSlider);
  
  ////////////////////////////////////////////////////////
  
  // Function to close the alert message when close button is clicked
  document.addEventListener("DOMContentLoaded", function () {
    const closeButtons = document.querySelectorAll(".close-alert");
    closeButtons.forEach(function (button) {
      button.addEventListener("click", function () {
        const alert = this.parentElement; // Get the parent alert element
        alert.classList.remove("show"); // Remove the 'show' class to hide the alert
        alert.classList.add("hide"); // Add the 'hide' class to the alert
        setTimeout(function () {
          alert.remove(); // Remove the alert element from the DOM after hiding it
        }, 500); // Adjust the delay (in milliseconds) as needed
      });
    });
  });
  