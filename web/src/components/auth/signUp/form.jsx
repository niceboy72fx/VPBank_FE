import * as React from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";



// TODO remove, this demo shouldn't need to reset the theme.
const defaultTheme = createTheme();

export const SignUpForm = ({handleLogin}) => {

   const [checkEmail, setCheckEmail] = React.useState({
    error: false,
    content: "",
  });

  const [checkPassword, setCheckPassword] = React.useState({
    error: false,
    content: "",
  });

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const formData = {
      first_name: data.get("firstName"),
      last_name: data.get("lastName"),
      email: data.get("email"),
      password: data.get("password"),
      re_password: data.get("re-password"),
      phone_number: data.get("phone"),
    }
    if (formData.email === "" && formData.password === "") {
      setCheckEmail({
        error: true,
        content: "Email is not valid !",
      });
      setCheckPassword({
        error: true,
        content: "Password must be length > or = 8 characters !",
      });
    } else {
      handleLogin(formData);
    }
  }


  const eventListenEmailInput = (event) => {
    if (EMAIL_REGX.test(event.target.value) === false) {
      setCheckEmail({
        error: true,
        content: "Email is not valid !",
      });
    } else if (EMAIL_REGX.test(event.target.value) === true) {
      setCheckEmail({
        error: false,
        content: "",
      });
    }
  };

  const eventListenPasswordInput = (event) => {
    if (PASSWORD_REGX.test(event.target.value) === false) {
      setCheckPassword({
        error: true,
        content: "Password must be length > or = 8 characters !",
      });
    } else if (PASSWORD_REGX.test(event.target.value) === true) {
      setCheckPassword({
        error: false,
        content: "",
      });
    }
  };


  const eventListenPhoneNumberInput = (event) => {
    if (PASSWORD_REGX.test(event.target.value) === false) {
      setCheckPassword({
        error: true,
        content: "Password must be length > or = 8 characters !",
      });
    } else if (PASSWORD_REGX.test(event.target.value) === true) {
      setCheckPassword({
        error: false,
        content: "",
      });
    }
  };

    const eventListenNameInput = (event) => {
    if (PASSWORD_REGX.test(event.target.value) === false) {
      setCheckPassword({
        error: true,
        content: "Password must be length > or = 8 characters !",
      });
    } else if (PASSWORD_REGX.test(event.target.value) === true) {
      setCheckPassword({
        error: false,
        content: "",
      });
    }
  };

  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign up
          </Typography>
          <Box
            component="form"
            noValidate
            onSubmit={handleSubmit}
            sx={{ mt: 3 }}
          >
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  autoComplete="given-name"
                  name="firstName"
                  required
                  fullWidth
                  id="firstName"
                  label="First Name"
                  autoFocus
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  required
                  fullWidth
                  id="lastName"
                  label="Last Name"
                  name="lastName"
                  autoComplete="family-name"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="email"
                  label="Email Address"
                  name="email"
                  autoComplete="email"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="phone"
                  label="Phone Number"
                  name="phone"
                  autoComplete="email"
                  type="phone"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name="password"
                  label="Password"
                  type="password"
                  id="password"
                  autoComplete="new-password"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name="re-password"
                  label="Re-type Password"
                  type="password"
                  id="re-password"
                  autoComplete="new-password"
                />
              </Grid>
      
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign Up
            </Button>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Link href="/login" variant="body2">
                  Already have an account? Sign in
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>

      </Container>
    </ThemeProvider>
  );
};
