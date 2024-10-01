document.addEventListener("DOMContentLoaded", () => {
	const selectors = {
		openMenu: ".js-menuOpen",
		closeMenu: ".js-menuClose",
		mobileMenu: ".js-pushmobileMenu",
		navOverlay: ".js-navOverlay",
		openLevel: ".js-openLevel",
		backLevel: ".js-backLevel",
	};

	const elements = {
		openMenu: document.querySelector(selectors.openMenu),
		closeMenu: document.querySelectorAll(selectors.closeMenu), // Select all close buttons
		mobileMenu: document.querySelector(selectors.mobileMenu),
		navOverlay: document.querySelector(selectors.navOverlay),
		openLevel: document.querySelectorAll(selectors.openLevel),
		backLevel: document.querySelectorAll(selectors.backLevel),
	};

	function toggleMenu(isOpen) {
		if (elements.mobileMenu) {
			elements.mobileMenu.classList.toggle("isOpen", isOpen);
		}
		if (elements.navOverlay) {
			elements.navOverlay.classList.toggle("active", isOpen);
		}
		if (!isOpen) {
			// Close all levels if the menu is being closed
			closeAllNavLevels();
		}
	}

	function closeAllNavLevels() {
		const allNavLevels = document.querySelectorAll(".pushNav");
		allNavLevels.forEach((level) => {
			level.classList.remove("isOpen");
		});
	}

	function handleOpenMenu(e) {
		e.preventDefault();
		toggleMenu(true);
	}

	function handleCloseMenu() {
		toggleMenu(false);
	}

	if (elements.openMenu) {
		elements.openMenu.addEventListener("click", handleOpenMenu);
	}

	// Attach event listeners to all close buttons
	elements.closeMenu.forEach((closeButton) => {
		closeButton.addEventListener("click", handleCloseMenu);
	});

	elements.openLevel.forEach((item) => {
		item.addEventListener("click", () => {
			const nextNavLevel = item.nextElementSibling;
			if (nextNavLevel) {
				nextNavLevel.classList.add("isOpen");
			}
		});
	});

	elements.backLevel.forEach((item) => {
		item.addEventListener("click", () => {
			const parentNavLevel = item.closest(".js-pushNavLevelBack");
			if (parentNavLevel) {
				parentNavLevel.classList.remove("isOpen");
				parentNavLevel
					.querySelectorAll(".isOpen")
					.forEach((childLevel) => childLevel.classList.remove("isOpen"));
			}
		});
	});
});
