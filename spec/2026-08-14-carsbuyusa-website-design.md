# carsbuyusa.com — Company Website Design

**Date:** 2026-08-14
**Status:** Approved by owner, in build

---

## Why this exists

A Ukrainian bank will not release a client's outgoing wire to Cars Buy USA Inc. without a company
website it can inspect. Direct payment from Ukrainian banks has only been possible since 2022, and
compliance departments verify every declared detail before releasing funds.

This is not a marketing site. It has one job:

> A compliance officer holding our invoice opens carsbuyusa.com and, within a minute, confirms that
> the company is real, that it is the same entity named on the invoice, and that the activity it
> describes is the activity the payment is for.

Everything in the design follows from that sentence.

### The check being run

The officer compares three things: the **invoice**, the **beneficiary bank account**, and the
**website**. A mismatch on any pair stops the payment. The specific failure mode we are designing
against is a *plausible* site that describes a different business from the one the invoice bills for.

### What this site is not

It does not replace `google-workspace-setup/WEBSITE-BRIEF-QUESTIONS.md`, the full marketing brief for
an exclusive-car sourcing site. That brief is still unanswered and describes a different, larger
project. This site is deliberately narrower and can be replaced or expanded later.

---

## Positioning decision

The July 2026 brief positioned the site around **sourcing rare and exclusive cars**, with salvage
deliberately excluded. For this purpose that positioning is wrong, and the owner agreed to change it.

Invoices bill overseas buyers for specific auction vehicles: VIN, lot number, odometer and odometer
condition, salvage-title flag, purchase amount, departure date, "sold to" address abroad. A site
selling collector-car hunts does not explain that invoice.

**Approved positioning: export-led, with sourcing secondary.**

- **Primary (matches the invoice):** we purchase vehicles at US auto auctions on behalf of clients
  outside the United States, and handle title, export documentation, and shipping.
- **Secondary:** we source a specific vehicle to order when a client asks for one.

### Salvage titles — deliberate deviation from the earlier brief

The earlier brief kept salvage off the site entirely. This design **discloses title status** instead,
in one restrained line: every invoice states whether the vehicle carries a clean or salvage title.

Rationale: our invoices carry a salvage-title field, so a site that implies only clean-title vehicles
creates the exact mismatch this project exists to prevent. Stated plainly, disclosure reads as
diligence rather than as a caveat.

This is flagged as a reversible decision. It is one entry in `content.py` and can be removed without
touching anything else.

---

## Truthfulness constraints

The site publishes only facts that are true and independently checkable. This is a design constraint,
not a preference: fabricated history is precisely what these checks detect, and being caught costs
more than a thin site.

**Published (verified, sourced from `cbusa-audit/templates/agreement.html:154`):**

| Fact | Value |
|---|---|
| Legal name | Cars Buy USA Inc. |
| Address | 300 W Service Rd, 2nd Floor, Staten Island, NY 10314, USA |
| EIN / Tax ID | 92-3260990 |
| State of incorporation | New York |

**Owner must supply before launch:** public phone number, NY DOS entity ID, incorporation date.

**Never published, at any point:**

- Bank or wire details. These belong in the invoice sent directly to the client. A public page
  carrying them is raw material for payment-redirection fraud against our own clients.
- Any dealer, broker, or buying-agent licence claim. Whether the company holds one is unresolved in
  the brief (§G1). Claiming a licence we do not hold is a regulatory problem, not a marketing one.
  The copy therefore describes *what we do* and never *under what licence*.
- Founding year, cars-sourced counts, years in business, client names, testimonials, staff photos,
  or any figure not confirmed by the owner.
- Stock photography of vehicles we did not handle. The design carries itself typographically. Real
  photographs can be added later and will strengthen it considerably.

**Placeholder policy.** A fact that is not yet supplied is `None` in `content.py`, and the build
**omits its row entirely** and prints a warning. The word "TBD" must never reach a published page —
on a site whose only purpose is verification, a placeholder is worse than an absence.

---

## Languages

Three: **English** (default, at `/`), **Ukrainian** (`/uk/`), **Russian** (`/ru/`). Ukrainian precedes
Russian in the switcher; the primary client base is Ukrainian.

**All three must state identical facts.** An officer running the pages through a translator and
finding that the English and Russian describe subtly different businesses is worse off than with one
language. This is enforced structurally rather than by discipline: the identity facts live in a
single `FACTS` dictionary, are never translated, and are rendered into all fifteen pages from that
one source. Only prose is per-language, and every language supplies the same page and block
structure.

---

## Architecture

Static HTML and CSS. No framework, no JavaScript, no runtime, no build step for the deployed output
beyond a generator run. Nothing can break in production because there is nothing executing.

A generator rather than fifteen hand-written files, for two reasons that are requirements rather than
convenience: it makes cross-language fact consistency structural, and it turns the outstanding
placeholders (phone, DOS ID, incorporation date) into a one-line edit in one file instead of fifteen
correlated edits.

```
website/
  build.py            generator — stdlib only, no dependencies
  content.py          FACTS + all copy for all three languages
  assets/site.css     stylesheet source
  spec/               this document — outside docs/, therefore never published
  docs/               GENERATED. GitHub Pages serves this folder.
    CNAME .nojekyll index.html how-it-works.html services.html company.html contact.html
    uk/ ru/           same five pages each
    assets/site.css
```

`docs/` is the Pages source folder because GitHub only supports repository root or `/docs` for branch
deploys. The spec sits in `spec/` specifically so that it stays unpublished — internal planning notes
on a compliance site would be an unforced error.

### Content model

Copy is data, not markup. Each page is a list of typed blocks (`prose`, `steps`, `cards`, `facts`,
`list`), so a language cannot accidentally acquire or lose a section: the structure is asserted at
build time across all three.

---

## Pages

| Page | Job in the compliance check |
|---|---|
| **Home** | States the business in one sentence matching the invoice purpose. Three-step summary, markets served. |
| **How it works** | Purchase → title and documents → transport → ocean freight → delivery. Includes *What appears on every invoice*, listing the exact fields our invoices carry. This is the page that answers "why is this company being paid?" |
| **Services** | Auction purchase, export documentation, transport and freight. Then sourcing to order, secondary. |
| **Company** | Legal identity: entity name, EIN, registered address, state and details of incorporation, markets served. The page an officer screenshots. |
| **Contact** | Email on `@carsbuyusa.com`, phone, physical address, business hours. |

**Every footer carries the full company identity block**, identical on all fifteen pages, so the
identifying facts are present wherever the officer lands.

**No contact form.** A form needs a backend; a form that silently fails is worse than no form. Email
and phone only.

**The published email address must exist and be monitored.** An address that bounces during a
verification check fails that check on its own. `info@carsbuyusa.com` is assumed; the owner must
confirm the mailbox is live on the existing Google Workspace tenant.

**Third-party marks.** Copart and IAA are named descriptively, as the auctions we buy from, with an
explicit non-affiliation note in the footer. Naming them helps the invoice match; implying a
partnership would be a false claim.

---

## Deployment

GitHub Pages, custom domain `carsbuyusa.com`, repository under the `value-deliver` organisation.

**DNS: MX records must not be touched.** `carsbuyusa.com` runs Google Workspace and email is live.
Only the four A records, four AAAA records, and the `www` CNAME change. Any edit to MX breaks company
email, which during a payment-verification check would be the worst possible time.

HTTPS via Pages-provisioned certificate; "Enforce HTTPS" enabled. A certificate warning during a
compliance check is disqualifying.

---

## Known weaknesses, stated rather than papered over

1. **The site is visibly new.** Domain age and archive history are checkable. There is no honest
   remedy and no dishonest one worth taking. A truthful new site passes these checks routinely.
2. **No photographs of real vehicles.** The single biggest available improvement. Requires owner
   supply, and vehicle photos must not show readable plates, faces, or customer paperwork.
3. **Licence position unresolved.** Copy is written to be accurate whichever way §G1 resolves, but if
   the company does hold a dealer licence, saying so would materially strengthen the page.

---

## Success criteria

1. `carsbuyusa.com` resolves over HTTPS with a valid certificate, in all three languages.
2. Legal name, address, and EIN on the site match the invoice and the beneficiary account exactly.
3. The activity described matches the payment purpose an officer reads on the invoice.
4. Company email continues to deliver — MX records verified unchanged after the DNS edit.
5. No unfilled placeholder appears on any published page.
6. The three languages state identical facts.
