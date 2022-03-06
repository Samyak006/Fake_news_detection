const express = require('express');
const HomeController = require('../controller/HomeController');
const router = express.Router();

router.get("/",HomeController.normal)
router.post("/submitText",HomeController.submitText)
router.post("/submitImage",HomeController.submitImage)


module.exports = router;