# barcode-media-player
A client for contolling media players via barcodes

## The Dream
I wish to have a media playing experience wherein I can flip through a binder filled with printed pages listing off my albums, playlists, songs, and movies. To select, I simply scan a barcode and the music or movie starts playing.

These pages would provide a tactile experience with album artwork, liner notes, and song listings.

There would also be basic media controls like play, pause, stop, next, back, shuffle, volume, etc.

A "Party Mode" could exist wherein scanning a starting code enters party mode and subsequent album/song scans would add to a shuffled playlist.
    
These are all just dreams right now, though. Look at the Roadmap below to see what's complete and what's to come.

## A Suite of Tools

`bmp-config` - A tool to configure global settings, add albums and playlists, interface with Spotify to import albums, etc.

`bmp-config-gtk` - A GTK interface to `bmp-config`

`bmp-listener` - Daemon that listens to barcode reader and controls media players

`bmp-pdf` - Creates PDF file for printing containing albums, artwork, lyrics, and barcodes

## A modular design

Player modules allow `barcode-media-player` to interface with various media services including:

 * Spotify
 * VLC (for local media)

## Roadmap

## Internal Design

### Features of PDF
 * Table of contents
     * Small barcodes embedded inline allow for quick selection
 * Sections (like Albums, Playlists, Movies, etc)
     * Sections are configurable.  You can add different ones, reorder, rename, *etc.*
     * Media objects can have belong to more than one section
 * Collection pages
     * Each `Collection` - which could represent an Album, Playlist, TV Series, Box Set, *etc.* - will have its own page
     * If lyrics or descriptions are defined for the individual items in the collection, they will be listed on the back

### `MediaObject`s
 * The generic object covering all media types and sources
 * Sub-forms are `Song`, `Clip`, `Movie`, `Collection`
 * All `MediaObject`s have a `.provider` which can be one of:
     * "spotify"
     * "local"
 * `Collection`s contain multiple `Song`s, `Clip`s, or `Movie`s
     * Currently, collections contain objects with the same provider - this restriction may be overcome in the future.

### One-provider restriction
The reasoning behind the one-provider restriction is that `barcode-media-player` is mainly a manipulator of already-existent media players.  As such, it lets them control the flow of music while music is playing.  Features like playlists, shuffling, next, back, etc. are all passed through to the proper media player.  It would be a different type of difficulty for `barcode-media-player` itself to know what's playing and be able to react to a song's completion to pause the media player and start another one.

That being said, this would be a really neat feature that may come in the future.

### To Do
* Create initial documentation and to-do list
* Flesh out main points on roadmap