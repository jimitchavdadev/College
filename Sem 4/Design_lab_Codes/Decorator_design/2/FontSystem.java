// Component Interface
interface Font {
    String getStyle();
}

// Concrete Component
class BaseFont implements Font {
    @Override
    public String getStyle() {
        return "Normal";
    }
}

// Decorator
abstract class FontDecorator implements Font {
    protected final Font decoratedFont;

    public FontDecorator(Font font) {
        this.decoratedFont = font;
    }

    @Override
    public String getStyle() {
        return decoratedFont.getStyle();
    }
}

// Concrete Decorators
class BoldFont extends FontDecorator {
    public BoldFont(Font font) {
        super(font);
    }

    @Override
    public String getStyle() {
        return "Bold, " + super.getStyle();
    }
}

class ItalicFont extends FontDecorator {
    public ItalicFont(Font font) {
        super(font);
    }

    @Override
    public String getStyle() {
        return "Italic, " + super.getStyle();
    }
}

class UnderlineFont extends FontDecorator {
    public UnderlineFont(Font font) {
        super(font);
    }

    @Override
    public String getStyle() {
        return "Underline, " + super.getStyle();
    }
}

// Client code
public class FontSystem {
    public static void main(String[] args) {
        // Create base font
        Font baseFont = new BaseFont();
        System.out.println("Base Font Style: " + baseFont.getStyle());

        // Apply decorators
        Font boldItalicFont = new BoldFont(new ItalicFont(baseFont));
        System.out.println("Bold Italic Font Style: " + boldItalicFont.getStyle());

        Font underlineFont = new UnderlineFont(baseFont);
        System.out.println("Underline Font Style: " + underlineFont.getStyle());

        Font boldUnderlineFont = new BoldFont(new UnderlineFont(baseFont));
        System.out.println("Bold Underline Font Style: " + boldUnderlineFont.getStyle());
    }
}
