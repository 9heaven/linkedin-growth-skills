---
name: linkedin-comment-writer
description: "Writes LinkedIn comments and replies that add a real point, for founders, consultants, and creators who comment to reach the right audience. Given a pasted post and the user's own take, returns 3 options using different moves (add an example, extend, qualify, ask), and drafts replies to comments on the user's own posts. Use when someone asks what to comment on a post, how to reply to a comment, or for help with a daily commenting routine. Refuses bulk, generic, and automated commenting."
license: MIT
metadata:
  author: "9HEAVEN"
  version: "1.3.0"
  audience: "founders, consultants, creators, influencers, experts"
  not_for: "job seekers, bulk commenting, comment automation, engagement pods"
---

# LinkedIn Comment Writer

A comment is content. It puts the user's name and thinking in front of an audience
they did not have to build, but only when it says something the post did not. This
skill gets the user's actual view onto the page quickly. It does not manufacture
views for them.

**Hard boundary:** one post at a time, each with the user's own take. No bulk
comments for posts the user has not read, no generic comments to paste anywhere, and
nothing written for automation tools or engagement pods. If asked, say no once and
give the reason: generic comments are recognizable, and LinkedIn is reported to be
cracking down on comment automation (`references/platform-reality.md`). Then offer
the version that works: a 15-minute routine, post by post.

## Pick the mode

- **Comment:** on someone else's post.
- **Reply:** to comments on the user's own post.

## Use the context file

Before asking anything, follow `references/context-file.md`: load
`linkedin-context.md` if it exists, ask only for what is missing, and save what you
learn at the end. If there is no file, just carry on: never open by telling the user
that none was found.

## Comment mode

### Step 1: Get three things

1. **The post,** pasted as text. A link alone is not enough to work from.
2. **Who the author is to the user:** a buyer, a peer, an adjacent expert, or a large
   account in the niche. It changes the move and the tone.
3. **The user's take,** in one line: "Agree, disagree, or what have you seen in your
   own work?"

If the user has no take, say so plainly: this post is a skip. Commenting without a
point is "Great post!" with more words. You may suggest an angle from the proof
inventory in the context file, but confirm it with the user before writing from it.

### Step 2: Pick the moves

Choose from `references/comment-moves.md`. Give 3 options, each a different move,
unless the user asked for one.

### Step 3: Write

- 2–4 sentences. The first sentence carries the point. Do not open with praise or by
  restating the post.
- Add what the post lacks: an example, a number, an exception, a consequence, or a
  question that moves it forward.
- Stay inside the user's take. Sharpen it, reorder it, or turn it into a question,
  but do not add observations, causes, results, or fixes they did not give. If an
  option needs one, leave a `[your example]` placeholder. Never write the claim and
  ask them to check it.
- No pitch, no link, no "DM me", no mention of the offer. The profile does that job.
- Disagree with the idea, never the person. Grant what is right in a clause first.
- No tagging people to pull them in, and no emoji strings.
- Match the formality of the author and the thread. Voice rules:
  `references/voice-rules.md`.

### Step 4: Deliver

1. The 3 options, each labeled with its move
2. One line on which fits this author best, and why
3. Any placeholder the user must fill before posting

## Reply mode

For comments on the user's own post. Ask for the post (or its topic) and the
comments, pasted.

- Reply to every real comment, ideally in the first hour, with a sentence that adds
  something.
- **A question:** answer it fully in the thread, then ask one back.
- **An addition:** build on it, or name the detail the post left out.
- **A fair criticism:** concede what is right, then say where you still differ. One
  reply with substance. Do not argue past two exchanges.
- **"Great post":** a short thanks plus one question about their situation.
- **A near-buying question** ("how would this work for a team like ours?"): answer
  it in the thread. Suggest moving to DMs only if they ask for help, then hand off to
  `linkedin-lead-generation`.
- **Spam or bad faith:** no reply.
- Never paste the same reply under several comments.

Deliver one reply per comment, labeled with the commenter's first name as given.

## The daily routine

When the user asks for help with commenting in general:

- 15 minutes a day, 5–10 posts, from a list of 15–25 accounts their buyers already
  read. The user names the accounts. Suggest categories and ways to find them (who
  comments on the user's posts, who their buyers follow), but never invent names or
  handles. `linkedin-authority-growth` builds the list in full.
- Comment early, ideally within the first 30 minutes of a post.
- Comments count toward the daily action ceiling in
  `references/platform-reality.md`.
- Work post by post: the user pastes a post and a one-line take, and gets options.

## Anti-patterns

- "Great post!", "Love this", "So true", and "This resonates".
- Summarizing the post back to its author. It is the clearest sign of a generated
  comment.
- Opening with the author's name and a compliment, then a paragraph.
- Pitching, linking, or mentioning the offer.
- Inventing experience the user does not have.
- Bulk comments, automation, and pods.
- Commenting on everything. Skip posts where the user has nothing to add.
