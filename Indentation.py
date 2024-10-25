def create_default_image(self, size: Union[str, int] = "default", pattern: str = "grid") -> Image.Image:
    """Create a default image if doesn't want to import one.

    Args:
        size (str or int): Size of the image. If "default", use the default size.
        pattern (str): Pattern to generate. Can be "grid", "noise", "cercle", or "rectangle".

    Returns:
        Image.Image: The generated image.
    """
    if size == "default":
        size = self.axe_X

    abs_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    folder = os.path.join(abs_path, 'images')
    self.img_name = os.path.join(folder, 'default.png')

    axe_X = 1000  # int(self.axe_X)
    axe_Y = 500  # self.axe_X // 2

    # Initialize nbr_rect here
    nbr_rect = 40  # You can adjust this value as needed

    if pattern == "noise":
        pixels = np.random.randint(0, 255, (axe_Y, axe_X, 3))
        self.img_original = Image.fromarray(pixels.astype('uint8'), 'RGB')

    elif pattern in ("grid", "cercle", "rectangle"):
        self.img_original = Image.new('RGB', (axe_X, axe_Y), color=255)
        Drawer = ImageDraw.Draw(self.img_original)
        Drawer.rectangle((0, 0, axe_X / 2, axe_Y / 2), fill="yellow")
        Drawer.rectangle((0, axe_Y / 2, axe_X / 2, axe_Y), fill="green")
        Drawer.rectangle((axe_Y, 0, axe_X, axe_Y / 2), fill="blue")
        Drawer.rectangle((axe_Y, axe_Y / 2, axe_X, axe_Y), fill="red")

        if pattern == "grid":
            for i in range(0, axe_X, axe_X // nbr_rect):
                Drawer.line((i, 0, i, axe_Y), fill="black", width=2)
            for i in range(0, axe_Y, axe_Y // (nbr_rect // 2)):
                Drawer.line((0, i, axe_X, i), fill="black", width=2)
        else:
            for i in range(0, axe_X, axe_X // nbr_rect):
                if pattern == "cercle":
                    Drawer.ellipse((i, i / 2, axe_X - i, axe_Y - i / 2), outline="black")
                elif pattern == "rectangle":
                    Drawer.rectangle((i, i / 2, axe_X - i, axe_Y - i / 2), outline="black")

    else:
        raise ValueError("pattern parameter must be: grid, noise, cercle or rectangle")

    if self.img_original is None:
        raise ValueError("img_original is None!")

    self.img_debut = self.img_resize(size)
    return self.img_debut