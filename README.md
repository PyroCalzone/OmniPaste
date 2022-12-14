<a name="readme-top"></a>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/PyroCalzone/OmniPaste">
    <img src="assets/icon.png" alt="Logo" width="120" height="120">
  </a>
 

<h3 align="center">OmniPaste</h3>

  <p align="center">
    Up to 10 simultaneous copy and paste clipboards.
    <br />
    <a href="https://github.com/PyroCalzone/OmniPaste/issues">Report Bug</a>
    ·
    <a href="https://github.com/PyroCalzone/OmniPaste/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


### Prerequisites

* system_hotkey
  ```sh
  pip install system_hotkey
  ```
* pywin32
  ```sh
  pip install pywin32
  ```
* keyboard
  ```sh
  pip install keyboard
  ```
* pyperclip
  ```sh
  pip install pyperclip
  ```
* pystray
  ```sh
  pip install pystray
  ```
* Pillow
  ```sh
  pip install Pillow
  ```

### Installation

1. Download the application:
   1. Head to our [releases page](https://github.com/PyroCalzone/OmniPaste/releases).
   2. Download the newest release.
   3. OmniPaste away!
2. Build the source:
   1. Clone the repo
    ```sh
    git clone https://github.com/PyroCalzone/OmniPaste.git
    ```
    2. Download the Prerequisites.
    3. Modify system_hotkey to add grave keybind (0xC0) OR download [my fork](https://github.com/PyroCalzone/system_hotkey_fix).
    3. OmniPaste away!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use CTRL+\`(Grave/Tilde) to switch between OmniPaste key-binds and the active program's key-binds.<br/>
     `CTRL + ALT + Number` to copy<br/>
     `CTRL + Number` to paste

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Register Key-binds
- [x] Key-bind Toggle
- [x] Copy Feature
- [x] Paste Feature
- [x] Copied Text Manipulation (Prevent newlines from sending messages on messengers)
- [ ] GUI to identify which key-bind holds which paste
- [x] Keybind switch notification


See the [open issues](https://github.com/PyroCalzone/OmniPaste/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Pyro - [Discord Server](https://discord.gg/Uca97Tf3tp) - pyrocalzoneemail@gmail.com

Project Link: [https://github.com/PyroCalzone/OmniPaste](https://github.com/PyroCalzone/OmniPaste)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/PyroCalzone/OmniPaste.svg?style=for-the-badge
[contributors-url]: https://github.com/PyroCalzone/OmniPaste/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/PyroCalzone/OmniPaste.svg?style=for-the-badge
[forks-url]: https://github.com/PyroCalzone/OmniPaste/network/members
[stars-shield]: https://img.shields.io/github/stars/PyroCalzone/OmniPaste.svg?style=for-the-badge
[stars-url]: https://github.com/PyroCalzone/OmniPaste/stargazers
[issues-shield]: https://img.shields.io/github/issues/PyroCalzone/OmniPaste.svg?style=for-the-badge
[issues-url]: https://github.com/PyroCalzone/OmniPaste/issues
[license-shield]: https://img.shields.io/github/license/PyroCalzone/OmniPaste.svg?style=for-the-badge
[license-url]: https://github.com/PyroCalzone/OmniPaste/blob/master/LICENSE
