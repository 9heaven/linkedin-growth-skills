---
name: linkedin-post-writer
description: "Writes one LinkedIn post from a rough idea, notes, or a client result, or reviews a draft before it is published, for founders, consultants, and creators. Picks the format, drafts in the user's voice, offers alternative hooks, and scores drafts on an 8-point rubric with the top fixes. Use when someone asks to write, draft, edit, improve, or review a LinkedIn post, or asks for a hook. Never invents numbers or clients, and refuses engagement bait. Not for job seekers."
license: MIT
metadata:
  author: "9HEAVEN"
  version: "1.3.0"
  audience: "founders, consultants, creators, influencers, agency owners"
  not_for: "job seekers, engagement bait, bulk post generation"
---

# LinkedIn Post Writer

Turn the user's real material into one post worth publishing, or tell them honestly
whether a draft is ready. A post exists to start conversations with buyers, not to
collect reactions.

## Pick the mode

- **Write:** the user brings an idea, notes, a transcript, or a result. Go to Write
  mode.
- **Review:** the user pastes a draft and asks if it is good, or asks to improve it.
  Go to Review mode.
- **Hook only:** the user wants hooks for a post that exists. Give 3 in different
  shapes from `references/post-formats.md` and stop.

For a plan (pillars, cadence, a calendar), hand off to `linkedin-content-strategy`.

## Use the context file

Before asking anything, follow `references/context-file.md`: load
`linkedin-context.md` if it exists, ask only for what is missing, and save what you
learn at the end.

## Write mode

### Step 1: Get the material

A post needs four things. Take them from the message and the context file, and ask
for the rest in one message:

1. **The point:** one idea. If the notes hold three, propose the strongest and park
   the others as future posts.
2. **The reader:** who it is for, by situation.
3. **The specifics:** the real numbers, names, and moments. These make the post
   theirs. If there are none, ask up to three questions that pull them out ("What
   was the number before and after?", "What did the client say?", "What did you get
   wrong first?"). If the user has none, write it as opinion or work in progress.
   Never make them up.
4. **The job:** which pillar it serves (authority, proof, teaching, personal) or an
   offer post, and what the reader should do next. Often that is nothing more than
   think or reply.

Voice: use the context file's voice notes, or ask for one past post. With no sample,
write plain and say that a sample would make it sound more like them.

### Step 2: Choose the format

Pick the template that matches the job from `references/post-formats.md`. The
default is a text post of 900–1,300 characters. Suggest an image when the proof is a
screenshot, and a carousel when the material is a framework or checklist.

### Step 3: Draft

- Body first, hook last. The hook must be true of the body.
- One idea. Cut anything that serves a second one.
- Specifics over adjectives. Every number and name comes from the user, or stays a
  `[your number]` placeholder.
- Paragraphs of 1–3 sentences, with varied length. No wall of one-liners.
- End where the idea ends: a takeaway, a real question the user wants answered, or a
  clear next step. Never "Agree?", "Thoughts?", or a request for likes.
- Links and assets go in the first comment. Write that comment too.
- Do not add hashtags or emoji unless the user's own posts use them.
- Voice rules: `references/voice-rules.md`.

### Step 4: Check before delivering

Score your own draft with `references/post-review-rubric.md`. Fix anything under 2
that you can fix without new information, and clear every hard fail. Count the
characters.

### Step 5: Deliver

1. The post, ready to paste
2. Two alternative hooks, each in a different shape
3. The first-comment text, if there is a link or an asset
4. One line listing any placeholder that still needs their number
5. One line: be available for 20 minutes after posting to reply to every comment

Nothing else. Do not explain why the post is good.

## Review mode

### Step 1: Read it whole

Name the draft's one idea and its job. If the context file does not say who the
reader is and the draft does not make it obvious, ask that one question.

### Step 2: Score it

Score the 8 criteria in `references/post-review-rubric.md` from 0 to 2, and check the
hard fails.

### Step 3: Deliver

1. **Verdict** in one line with the score out of 16: Publish, Fix first, or Rewrite
2. **Rubric table:** criterion, score, and a note only where the score is under 2
3. **Top fixes:** at most 3, ranked by impact, each quoting the line and giving the
   change
4. **Edited version:** the smallest set of edits that clears the fixes. Keep their
   phrasing. If the draft states a statistic about the world with no source, ask for
   the source or cut the line. Their own results are theirs to state.
5. Two alternative hooks, only if the Hook score is under 2

If the verdict is Publish, say so and stop. Do not rewrite a post that works just to
make it different.

## Anti-patterns

- Inventing a number, a client, or an anecdote to make the post land.
- Polishing the user's voice into generic LinkedIn voice.
- Engagement-bait endings. LinkedIn reduces the reach of posts that ask for
  engagement, and they attract the wrong audience.
- Three ideas in one post.
- A hook the body does not pay off.
- Bulk requests with no material ("write me 30 posts"). Hand off to
  `linkedin-content-strategy` for pillars and topic seeds, then write a few at a
  time from real material.
