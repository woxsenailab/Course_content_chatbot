import React from "react";
import { BsLinkedin, BsTwitterX, BsYoutube } from "react-icons/bs";

const Footer: React.FC = () => {
  return (
    <div className="border-t-2 text-base-content p-10 bg-black">
      <footer className="footer footer-center p-4 mx-auto rounded-2xl">
        <nav className="mb-6">
          <div className="flex items-center justify-center gap-16">
            <a href="https://in.linkedin.com/school/woxsen-university/" className=" text-white hover:text-primary hover:scale-105 duration-300">
              <BsLinkedin size={24} />
            </a>
            <a href="https://x.com/Woxsen" className=" text-white hover:text-primary hover:scale-105 duration-300">
              <BsTwitterX size={24} />
            </a>
            <a href="https://www.youtube.com/c/WoxsenUniversity" className=" text-white hover:text-primary hover:scale-105 duration-300">
              <BsYoutube size={30}/>
            </a>
          </div>
        </nav>

        <aside className="flex items-center justify-center">
          <p className="text-white font-workSans">
            Copyright © {new Date().getFullYear()} - All rights Reserved by {" "}
            <span className="text-primary font-semibold font-workSans">
              Woxsen University
            </span>
          </p>
        </aside>
      </footer>
    </div>
  );
};

export default Footer;
