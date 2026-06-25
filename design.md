---
name: EduVibrant Professional
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#5b403e'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#8f706d'
  outline-variant: '#e3bebb'
  surface-tint: '#b81d27'
  primary: '#b51925'
  on-primary: '#ffffff'
  primary-container: '#d8363a'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb3ae'
  secondary: '#585e6f'
  on-secondary: '#ffffff'
  secondary-container: '#dadff3'
  on-secondary-container: '#5d6273'
  tertiary: '#006b29'
  on-tertiary: '#ffffff'
  tertiary-container: '#008735'
  on-tertiary-container: '#f7fff2'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ae'
  on-primary-fixed: '#410004'
  on-primary-fixed-variant: '#930015'
  secondary-fixed: '#dde2f6'
  secondary-fixed-dim: '#c1c6d9'
  on-secondary-fixed: '#151b29'
  on-secondary-fixed-variant: '#414756'
  tertiary-fixed: '#69ff87'
  tertiary-fixed-dim: '#3ce36a'
  on-tertiary-fixed: '#002108'
  on-tertiary-fixed-variant: '#00531e'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.25'
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  title-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-padding-mobile: 16px
  container-padding-desktop: 40px
  gutter: 16px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is built to bridge the gap between playful educational engagement and professional reliability. Inspired by the "PANDAI" visual identity, it balances high-energy action colors with a clean, airy structural framework.

The style is **Modern Corporate with a Friendly Edge**, utilizing a "Soft Minimalism" approach. It features high-contrast primary actions set against a very clean, spacious background. The emotional goal is to feel encouraging, accessible, and intellectually stimulating. Visual interest is maintained through subtle depth, vibrant accents, and significant negative space to reduce cognitive load, especially for mobile users.

## Colors

The palette is strategically divided to guide the user's eye through a clear hierarchy:

- **Primary (Vibrant Red):** Used for main "Call to Action" buttons and critical progress indicators. It conveys energy and urgency.
- **Secondary (Deep Navy):** Provides a grounded, professional anchor. Used for navigation bars, primary text, and high-contrast buttons (e.g., "Teacher Mode").
- **Tertiary (Fresh Green):** Represents success, completion, and positive feedback loops.
- **Neutral (Slate/White):** A sophisticated range of cool grays used for backgrounds and borders to keep the UI feeling "breathable" and modern.

The default mode is **Light**, optimizing for readability in varied lighting conditions typical of mobile educational environments.

## Typography

This design system uses **Plus Jakarta Sans** across all levels. It was selected for its modern, geometric construction and friendly, open counters which perform exceptionally well on small screens.

- **Headlines:** Use heavy weights (700-800) with slight negative letter-spacing for a bold, punchy look.
- **Body Text:** Uses a standard weight (400) with generous line heights to ensure long-form educational content is easy to digest.
- **Labels:** Uppercase and increased letter-spacing are applied to small labels (like the platform description) to maintain legibility despite the small scale.

## Layout & Spacing

The layout follows a **Fluid Grid** philosophy optimized for mobile-first delivery. 

1.  **Mobile (0-599px):** A single-column layout with 16px side margins. Elements are stacked vertically with consistent 24px (stack-md) spacing between major sections.
2.  **Tablet/Desktop (600px+):** Transitions to a centered max-width container (max 1200px) to prevent line lengths from becoming too long for comfortable reading. 

The vertical rhythm is based on an 8px square grid, ensuring all components align perfectly. Use "stack-lg" for separating primary modules (Hero vs. Content) and "stack-sm" for internal element grouping (Label vs. Input).

## Elevation & Depth

Visual hierarchy is achieved through **Soft Tonal Layers** and subtle shadows rather than harsh borders.

- **Surface Level 0 (Background):** Solid white or very light neutral (#F8FAFC).
- **Surface Level 1 (Cards):** White background with a "floating" effect created by an extremely soft, large-radius shadow (15% opacity, 20px blur, 4px vertical offset).
- **Depth Cues:** Interactive elements use a subtle inner glow or a thin, light gray outline (1px) to define boundaries without adding visual clutter.
- **Interaction:** On hover or tap, cards should elevate slightly (shadow increases) to provide tactile feedback.

## Shapes

The design system utilizes **Rounded** geometry to reinforce a friendly and safe environment for learning.

- **Primary Buttons:** Use a radius of 12px or more. For specific "Action Bullets," a pill-shape (fully rounded) is preferred.
- **Cards:** Defined by a consistent 1rem (16px) corner radius, creating a "soft rectangle" look.
- **Inputs:** Follow the button radius (12px) to maintain a cohesive interactive language.

## Components

### Buttons
- **Primary:** Solid vibrant red background with white text. High-visibility.
- **Secondary:** Solid dark navy background with white text. Used for secondary high-level actions.
- **Ghost/Tertiary:** Green borders with light green semi-transparent backgrounds for success actions or status indicators.

### Cards
Cards are the primary container for content. They must have a white background, the defined soft shadow, and 16px of internal padding. On mobile, cards should span the full width of the safe area.

### Input Fields
Inputs use a light neutral fill (#F1F5F9) and no border in their default state. Upon focus, they transition to a 2px solid primary color border.

### Chips/Badges
Small, fully rounded (pill) elements used for categories. Use the secondary navy color with high-transparency backgrounds for a subtle "tag" effect.

### Progress Bars
Utilize a multi-stop gradient (Blue-Green-Yellow-Red) as seen in the reference image to indicate a journey or platform complexity, reinforcing the "vibrant" brand pillar.